# 📊 Cohort Analysis — User Retention

## 📂 Data Source

- Full Dataset: [https://docs.google.com/spreadsheets/d/1vVQvIubB_4z9GV3FpbRrbg7Vbk301iJRHyrpeL7NJGA/edit?usp=sharing]
- Sample Dataset (for testing):  
  [sample_dataset.csv](../../data/sample/sample_dataset.csv)

  ## 🔗 Implementation

- 📓 Cohort Analysis Notebook (Pandas):  
  [Open Notebook](../../02_data_engineering_and_analysis/eda_analysis/notebooks/cohort_analysis.ipynb)

## 📌 Objective

To analyze **user retention behavior** by grouping users based on their signup period and tracking engagement over time.

---

## ⚠️ Data Note

The original KreditBee dataset was not available.
A **comparable fintech dataset** was used as a proxy for performing cohort analysis.

---

## 🧱 Step 1: Define Cohort

* Users are grouped based on **loan issue date (`issue_d`)**
* Due to limited monthly variation, cohorts are defined at a:

  * **Year level (`cohort_year`)**

👉 This acts as a proxy for user signup time

---

## 🔄 Step 2: Define User Activity (Proxy)

Since transaction-level activity is not available:

A user is considered **active if**:

* `total_pymnt > 0`
* `loan_condition = "Good Loan"`

👉 This indicates:

* User is financially engaged
* Loan is not defaulted

---

## 📈 Step 3: Calculate Retention

For each cohort:

* **Total Users** = Count of users in cohort
* **Active Users** = Users satisfying activity condition
* **Retention Rate** = Active Users / Total Users

---

## 📊 Cohort Retention Table

| Cohort Year | Total Users | Active Users | Retention Rate |
| ----------- | ----------- | ------------ | -------------- |
| 2007        | 139         | 95           | 0.683          |
| 2008        | 516         | 417          | 0.808          |
| 2009        | 1173        | 1003         | 0.855          |
| 2010        | 2822        | 2400         | 0.850          |
| 2011        | 4747        | 4031         | 0.849          |
| 2012        | 11777       | 9899         | 0.840          |
| 2013        | 29698       | 25575        | 0.861          |
| 2014        | 19128       | 17616        | 0.921          |

---

## 🔍 Step 4: Insights

* Retention improves from **2007 (68.3%) → 2009 (85.5%)**
* Stable retention observed between **2010–2012 (~84–85%)**
* Significant improvement in newer cohorts:

  * **2014 → 92.1% (highest)**

### 📌 Key Insight

Newer cohorts show **better retention**, indicating:

* Improved product experience
* Better risk profiling
* Stronger user quality

---

## ⚠️ Retention Drop Analysis

### Problem:

Retention drops significantly after initial engagement

---

## ❗ Possible Reasons

### 1. User Quality Issues

* High DTI users struggle with repayments
* Lower credit grade users disengage early

---

### 2. Pricing & Financial Burden

* High interest rates increase pressure
* Users drop after initial usage

---

### 3. Lack of Engagement

* Users unaware of repayment schedule
* No reminders or follow-ups

---

### 4. Poor Targeting

* Loans given to financially unstable users
* Low income / unstable employment

---

## ✅ Solutions

### 1. Improve Risk-Based Targeting

* Prioritize:

  * Low DTI
  * High credit grade
* Strengthen credit models

---

### 2. Optimize Pricing

* Flexible repayment options
* Risk-based interest rates

---

### 3. Improve Engagement

* EMI reminders
* Better onboarding experience

---

### 4. Incentivize Behavior

* Cashback for timely payments
* Rewards for early repayment

---

## 🧠 Advanced Validation

Hypotheses can be validated using segmentation:

* `dti` (debt-to-income ratio)
* `grade` (credit quality)
* `income_category`

👉 Compare retention across segments to validate drivers

---

## 🎯 Key Takeaways

* Cohort analysis helps understand **user lifecycle behavior**
* Retention trends indicate **product and risk improvements**
* Enables **data-driven decisions for engagement and growth**
