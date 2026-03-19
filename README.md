# 🚀 GitHub Repository Analytics Dashboard

![Dashboard Preview](./images/dashboard.png)

## 📊 Overview

This project presents a **Big Data Analytics Pipeline** built using **Hadoop, Python, and Power BI** to analyze GitHub repository data.

It extracts insights such as:

* 📌 Popular programming languages
* ⭐ Top repositories by stars
* 🔁 Most forked repositories
* 📈 Developer engagement trends

---

## 🧠 Problem Statement

GitHub hosts millions of repositories, generating large-scale data that is difficult to analyze using traditional tools.

This project solves the problem by:

* Using **Hadoop (HDFS + MapReduce)** for scalable data processing
* Applying **Python-based analytics** for insight generation
* Visualizing results using **Power BI dashboards**

---

## ⚙️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,docker,github" />
</p>

* 🐘 **Apache Hadoop** — Distributed storage & processing
* 🐳 **Docker** — Hadoop cluster setup
* 🐍 **Python (Pandas, Matplotlib)** — Data processing & visualization
* 📊 **Power BI** — Interactive dashboard
* 📁 **HDFS** — Data storage layer
* ⚡ **MapReduce** — Parallel data processing

---

## 🏗️ Project Architecture

```text
Dataset (CSV/Excel)
        ↓
HDFS (Hadoop Storage)
        ↓
MapReduce (Python - Mapper & Reducer)
        ↓
Processed Data
        ↓
Python Analytics (KPIs + Charts)
        ↓
Power BI Dashboard
```

---

## 📂 Project Structure

```
├── images/                 # Generated charts
├── analysis.py            # Data processing & KPI generation
├── mapper.py              # MapReduce mapper
├── reducer.py             # MapReduce reducer
├── visualize.py           # Visualization script
├── docker-compose.yml     # Hadoop setup
├── hadoop.env             # Environment config
├── run_pipeline.ps1       # Automation script
├── final_dataset.xlsx     # Clean dataset for Power BI
├── kpi_summary.txt        # KPI results
├── github-dashboard.pbix  # Power BI dashboard
```

---

## 🔥 Key Features

* ⚡ Distributed data processing using Hadoop
* 📊 Multiple analytics KPIs
* 📈 Interactive Power BI dashboard
* 🧠 Engagement metric (Stars + Forks)
* 🎯 Top-N filtering for insights

---

## 📊 Dashboard Insights

* Top programming languages on GitHub
* Repository popularity based on stars
* Contribution levels using forks
* Correlation between stars and forks
* Language-wise distribution

---

## 🧮 KPIs Generated

* Total Repositories
* Total Stars
* Total Forks
* Average Engagement
* Language Distribution
* Top Repositories

---

## ▶️ How to Run (Local Setup)

### 1️⃣ Prerequisites

* Docker installed
* Python 3.x
* Power BI Desktop

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/your-username/github-analytics-dashboard.git
cd github-analytics-dashboard
```

---

### 3️⃣ Start Hadoop (Docker)

```bash
docker-compose up -d
```

---

### 4️⃣ Run Pipeline

```bash
python analysis.py
python visualize.py
```

OR (Windows PowerShell):

```bash
.\run_pipeline.ps1
```

---

### 5️⃣ Open Dashboard

* Open `github-dashboard.pbix` in Power BI
* Load `final_dataset.xlsx` if required

---

## 🧠 How It Works

* Data is stored in **HDFS**
* MapReduce processes large datasets
* Python scripts generate KPIs and charts
* Power BI visualizes insights interactively

---

## 📌 Future Improvements

* 🔮 Add Machine Learning (Repo Recommendation)
* ☁️ Deploy on Cloud (AWS / GCP)
* 🔄 Real-time GitHub API integration

---

## 👨‍💻 Author

**Tanmay Dalvi**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
