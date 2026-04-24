import os
import sqlite3
import pandas as pd
from datetime import datetime

RAW_PATH = "data/raw/loan_final313_.csv"
OUTPUT_PATH = "data/processed/loans_cleaned.csv"
LOG_PATH = "logs/etl_log.txt"


def log(message):
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


def validate_data(df):
    if df.empty:
        raise ValueError("Dataset is empty")

    required_cols = ["loan_amount", "annual_inc", "term", "loan_condition"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return True


def run_etl():

    try:
        log("ETL started")

        # 🔹 Step 1: Load
        df = pd.read_csv(RAW_PATH)
        log("Data loaded")

        # 🔹 Step 2: Validate
        validate_data(df)
        log("Validation passed")

        # 🔹 Step 3: SQL Engine
        conn = sqlite3.connect(":memory:")
        df.to_sql("loans", conn, index=False)

        median_income = df['annual_inc'].median()

        # 🔹 Step 4: Transform
        query = f"""
        WITH YearlyStats AS (
            SELECT
                year,
                COUNT(*) * 1.0 AS total_loans,
                SUM(CASE WHEN loan_condition = 'Bad Loan' THEN 1 ELSE 0 END) AS bad_loans
            FROM loans
            GROUP BY year
        )
        SELECT
            id,
            year,

            -- Date handling
            substr(issue_d, 7, 4) || '-' || substr(issue_d, 4, 2) || '-' || substr(issue_d, 1, 2) AS issue_date,

            -- Term cleaning
            CAST(TRIM(REPLACE(term, 'months', '')) AS INTEGER) AS term_months,

            -- Categorical cleaning
            UPPER(TRIM(home_ownership)) AS home_ownership,

            -- Missing handling
            COALESCE(annual_inc, {median_income}) AS annual_inc,

            loan_amount,
            purpose,
            interest_rate,
            grade,
            total_pymnt,
            recoveries,
            region,

            -- Features
            (total_pymnt - loan_amount) AS profitability,

            CASE WHEN loan_condition = 'Bad Loan' THEN 1 ELSE 0 END AS risk_flag,

            (COALESCE(annual_inc, {median_income}) / NULLIF(loan_amount, 0)) AS income_to_loan_ratio,

            (bad_loans / total_loans) AS default_rate_indicator

        FROM loans
        JOIN YearlyStats USING(year)

        WHERE loan_amount IS NOT NULL
          AND interest_rate IS NOT NULL
          AND purpose IS NOT NULL;
        """

        cleaned_df = pd.read_sql(query, conn)
        log("Transformation completed")

        # 🔹 Step 5: Save
        os.makedirs("data/processed", exist_ok=True)
        cleaned_df.to_csv(OUTPUT_PATH, index=False)

        log("ETL completed successfully")

    except Exception as e:
        log(f"ETL FAILED: {e}")
        print("Error:", e)


if __name__ == "__main__":
    run_etl()