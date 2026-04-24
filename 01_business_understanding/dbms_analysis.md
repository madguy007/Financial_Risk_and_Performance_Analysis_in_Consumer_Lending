# 🗄️ DBMS & Data Architecture — FinTech Systems

## 📌 Objective

To design a **robust, scalable, and reliable database system** for a FinTech platform like KreditBee, ensuring data integrity, performance, and compliance.

---

## 🔒 ACID Properties

### 1. Transaction Failure (Fund Transfer Crash)

**Problem:**
A fund transfer is initiated but the app crashes midway.

**Solution:**

* **Atomicity:**
  The transaction is treated as a single unit.
  Either:

  * Debit + Credit both succeed
  * OR both fail

  👉 Prevents partial updates

* **Durability:**
  Once committed, the transaction is permanently stored
  Even after system crash

---

### 2. Concurrent Transactions (Double Payment Issue)

**Problem:**
User clicks “Pay EMI” multiple times simultaneously.

**Solution:**

* **Isolation:**
  Transactions are executed independently using isolation levels
  Prevents double deduction

* **Consistency:**
  Ensures database rules are maintained
  (e.g., balance never goes negative incorrectly)

---

## ⚡ Indexing

### Use Case: Real-Time Dashboards

**Problem:**
Querying large datasets slows performance.

**Solution:**

* Use **B-Tree indexing** on:

  * `userID`
  * `accountID`

👉 Enables fast data retrieval (milliseconds instead of full scan)

---

### Optimized Strategy

* Index frequently queried columns
* Avoid over-indexing to reduce update cost

---

## 📦 Partitioning

### 1. Large Transaction Tables

**Solution:**

* Use **Time-based (Range) Partitioning**
* Example:

  * `transactions_2024_Q1`
  * `transactions_2024_Q2`

👉 Benefits:

* Faster queries
* Efficient archiving

---

### 2. Data Residency Compliance

**Solution:**

* Use **Geo-partitioning**

👉 Example:

* Indian user data stored in India (RBI compliance)

---

## 🧩 Sharding

### 1. Scaling for High Traffic

**Solution:**

* Use **Horizontal Sharding (userID-based)**

Example:

* Users 1–5M → Server A
* Users 5M–10M → Server B

👉 Distributes load across servers

---

### 2. Challenge: Global Analytics

**Problem:**
Cross-shard queries are slow

**Solution:**

* Use **Data Warehouse** for analytics
* Avoid analytics on OLTP systems

---

## 🧱 Normalization vs Denormalization

### Normalization

* Reduces redundancy
* Maintains data integrity

👉 Example:

* Separate tables:

  * User_Profile
  * KYC
  * Loan

---

### Denormalization

* Improves read performance
* Used for reporting

👉 Trade-off:

* More storage vs faster queries

---

## 🏞️ Data Lake vs Data Warehouse

### Data Lake

* Stores raw/unstructured data
* Example:

  * Logs
  * Clickstream

---

### Data Warehouse

* Stores structured data
* Optimized for analytics

👉 Used for:

* Risk analysis
* Fraud detection

---

## 🔄 Data Ingestion

### 1. Real-Time Payments

**Solution:**

* Streaming pipeline (Kafka / Kinesis)

👉 Enables:

* Instant fraud detection

---

### 2. Daily Credit Score Updates

**Solution:**

* Batch ingestion (Airflow)

👉 Runs scheduled jobs

---

## ⚙️ ETL Pipeline Design

### Steps:

1. **Extract**

   * Pull data from APIs / sources

2. **Transform**

   * Clean data
   * Standardize formats
   * Remove duplicates

3. **Load**

   * Store in Data Warehouse

---

### Failure Handling

* Use **Checkpointing**
* Use **Idempotent operations**
* Apply **Upsert logic**

👉 Prevents duplication and ensures consistency

---

## 📚 Additional DBMS Concepts

### 1. Audit Logging

* Maintain **immutable logs**
* Track all changes (regulatory compliance)

---

### 2. ML Data Pipeline

* Use **Incremental ETL + CDC (Change Data Capture)**
* Update only changed data

---

### 3. Duplicate Detection

* Use:

  * Fuzzy matching
  * Composite keys

---

### 4. Real-Time Dashboard Architecture

**Solution:**

* Use **HTAP architecture**

Components:

* OLTP database (PostgreSQL)
* Materialized views
* Redis caching

👉 Ensures fast dashboard performance

---

## 🎯 Key Takeaways

* Strong DBMS design ensures **scalability and reliability**
* Separation of OLTP and OLAP is critical
* Modern systems use **streaming + batch + caching together**
* Data architecture directly impacts business performance
