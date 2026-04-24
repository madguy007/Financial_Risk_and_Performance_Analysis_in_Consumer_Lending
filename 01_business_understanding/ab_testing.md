# 🧪 A/B Testing — Loan Strategy Evaluation

## 📌 Objective

To evaluate whether a change in lending strategy (interest rate / loan conditions) improves **loan acceptance** without increasing **default risk**.

---

## 🧠 Business Problem

Does offering improved lending conditions (e.g., lower interest rate) increase loan acceptance while maintaining repayment quality?

---

## 🧩 Experiment Design

### Groups Definition

| Group         | Year | Strategy                    |
| ------------- | ---- | --------------------------- |
| A (Control)   | 2012 | Default lending conditions  |
| B (Treatment) | 2013 | Improved lending conditions |

---

## 📊 Hypothesis

* **H₀ (Null Hypothesis):**
  No change in loan acceptance or repayment behavior

* **H₁ (Alternative Hypothesis):**
  Improved lending conditions increase loan acceptance without increasing risk

---

## 📏 Evaluation Metrics

| Metric               | Column(s)                        | Purpose                       |
| -------------------- | -------------------------------- | ----------------------------- |
| Loan Acceptance Rate | `loan_condition`                 | Measures conversion           |
| Average Loan Amount  | `loan_amount`                    | Indicates borrower confidence |
| Repayment Behaviour  | `total_rec_prncp`, `total_pymnt` | Measures repayment quality    |
| Default Risk         | `recoveries`                     | Indicates portfolio risk      |

---

## 🧮 Data Preparation

* **Group A:** Records where `year = 2012`
* **Group B:** Records where `year = 2013`

👉 This simulates control vs treatment groups

---

## 📊 Results Comparison

| Group    | Loan Acceptance Rate | Avg Loan Amount | Repayment Behaviour | Default Risk |
| -------- | -------------------- | --------------- | ------------------- | ------------ |
| A (2012) | 0.841                | 13,535.92       | 11,466.81           | 138.90       |
| B (2013) | 0.861                | 14,740.59       | 10,666.37           | 119.25       |

---

## 🔍 Insights

* Loan acceptance increased (**0.841 → 0.861**)
* Average loan amount increased
* Repayment behaviour slightly decreased
* Default risk decreased

---

## 🎯 Key Insight

Group B shows:

* Higher loan adoption
* Higher loan size
* Slight drop in repayment
* Lower default risk

👉 Overall: **Growth improved without major risk increase**

---

## 🧾 Business Decision

### Recommendation:

Adopt the 2013 strategy **with caution**

---

### Action Plan:

1. Implement improved lending strategy
2. Monitor repayment trends closely
3. Segment users by risk level
4. Apply stricter checks for high-risk borrowers

---

## 🧠 Executive Summary

The updated lending strategy increases:

* Loan adoption
* Loan size

While:

* Keeping default risk stable

However:

* Slight decline in repayment behavior requires monitoring

---

## 🎯 Key Takeaways

* A/B testing helps validate business decisions
* Growth strategies must be evaluated with risk
* Data-driven experimentation improves product outcomes
