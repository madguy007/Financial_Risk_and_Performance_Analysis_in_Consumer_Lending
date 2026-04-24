# ⏰ ETL Automation — Cron Setup

## 📌 Objective

To automate the ETL pipeline so that data processing runs **periodically (daily/weekly)** without manual intervention.

---

## ⚙️ Automation Overview

The ETL pipeline is implemented using:

* Python script: `etl_automation.py`
* Logging system: `logs/etl_log.txt`
* Input data: `data/raw/`
* Output data: `data/processed/`

---

## 🔄 Workflow

1. Read raw dataset from `data/raw/`
2. Perform data cleaning and transformation
3. Generate cleaned dataset
4. Save output to `data/processed/`
5. Log execution details in `logs/etl_log.txt`

---

## 🖥️ Running ETL Manually

```bash id="run-manual"
python etl_automation.py
```

---

## ⏰ Automating with Cron (Linux / WSL)

### Step 1: Open Crontab

```bash id="open-cron"
crontab -e
```

---

### Step 2: Add Job

Example: Run ETL every day at 9 AM

```bash id="cron-job"
0 9 * * * /usr/bin/python3 /path/to/etl_automation.py
```

---

### Step 3: Save & Exit

Cron will now run automatically based on schedule.

---

## 🪟 Alternative (Windows Task Scheduler)

Since this project was developed on Windows:

### Steps:

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Set:

   * Trigger → Daily / Weekly
   * Action → Start a Program
4. Program:

```bash id="windows-python"
python
```

5. Arguments:

```bash id="windows-arg"
path\to\etl_automation.py
```

---

## 📊 Logging

* Logs stored in:

```bash id="log-path"
logs/etl_log.txt
```

### Purpose:

* Track execution status
* Debug failures
* Monitor pipeline health

---

## 🎯 Key Benefits

* Eliminates manual execution
* Ensures consistent data updates
* Simulates real-world data pipeline
* Improves reliability and scalability

---

## 🧠 Real-World Relevance

In production systems, ETL pipelines are scheduled using:

* Cron (Linux)
* Airflow (advanced orchestration)
* Cloud schedulers (AWS, GCP)

This implementation demonstrates a **foundational level of data pipeline automation**.
