# 📚 Amazon Books Analytics Dashboard

### End-to-End Data Analytics Project using Python, Pandas & Streamlit

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-blue?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 📖 Overview

Amazon Books Analytics Dashboard is an end-to-end data analytics project built using **Python**, **Pandas**, **Matplotlib**, and **Streamlit**.

The project analyzes Amazon's **Top 50 Bestselling Books (2009–2019)** to uncover meaningful insights about bestselling authors, genres, customer ratings, pricing trends, and reader engagement.

Rather than focusing only on visualizations, this project demonstrates the complete analytics workflow—from raw data preprocessing and exploratory analysis to business insights and an interactive dashboard.

---

# 🚀 Project Status

**Current Version:** **v1.0**

**Status:** ✅ Completed

### Implemented Modules

- Data Cleaning Pipeline
- Exploratory Data Analysis (EDA)
- Interactive Streamlit Dashboard
- Business Insights Report
- Data Visualizations
- Dataset Export

---

# 🎯 Project Objectives

The project aims to:

- Clean and preprocess raw datasets
- Perform exploratory data analysis
- Discover meaningful business insights
- Build reusable analysis modules
- Develop an interactive analytics dashboard
- Present findings through effective data visualization

---

# 📊 Analytics Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Visualizations
      │
      ▼
Business Insights
      │
      ▼
Interactive Dashboard
      │
      ▼
Filtered Data Export
```

---

# ✨ Features

## 📂 Data Cleaning

- Column Standardization
- Missing Value Validation
- Duplicate Detection
- Data Type Conversion
- Data Quality Checks
- Reusable Cleaning Pipeline

---

## 📈 Exploratory Data Analysis

Analysis includes:

- Bestseller Distribution
- Author Analysis
- Genre Comparison
- Rating Distribution
- Review Analysis
- Price Distribution
- Year-wise Trends
- Correlation Analysis
- Top Rated Books
- Most Reviewed Books

---

## 📊 Interactive Dashboard

Built using **Streamlit**.

Features include:

- KPI Cards
- Search by Book Title
- Search by Author
- Genre Filter
- Year Filter
- Rating Filter
- Price Filter
- Interactive Charts
- CSV Export

---

## 📄 Business Insights

The project generates insights such as:

- Most successful authors
- Genre popularity trends
- Customer review growth
- Price changes over time
- Rating distribution
- Relationship between price and reviews

---

# 💼 Business Questions Answered

The analysis explores questions such as:

- Which authors dominate Amazon's bestseller list?
- Which genre performs better?
- Does a higher price lead to better ratings?
- Which books receive the highest customer engagement?
- How have bestseller trends evolved over the years?
- Is there any relationship between reviews, ratings, and pricing?

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Streamlit | Interactive Dashboard |
| Jupyter Notebook | Exploratory Analysis |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📊 Dataset

**Source:**

Amazon Top 50 Bestselling Books (2009–2019)

Dataset Size

- 550 Records
- 7 Features

| Column | Description |
|----------|------------|
| Name | Book Title |
| Author | Author Name |
| User Rating | Average Rating |
| Reviews | Customer Reviews |
| Price | Book Price |
| Year | Bestseller Year |
| Genre | Fiction / Non Fiction |

---

# 📂 Project Structure

```text
amazon-books-analytics-dashboard/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda_notebook.ipynb
│
├── src/
│   ├── data_cleaning.py
│   └── eda_analysis.py
│
├── dashboard/
│   └── app.py
│
├── images/
│
├── reports/
│   └── business_insights.md
│
├── requirements.txt
└── README.md
```

---

# 🎓 Skills Demonstrated

- Data Cleaning
- Data Validation
- Exploratory Data Analysis
- Statistical Analysis
- Data Visualization
- Dashboard Development
- Business Insight Generation
- Python Programming
- Git Version Control
- Data Storytelling

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/amazon-books-analytics-dashboard.git

cd amazon-books-analytics-dashboard
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

### Launch Jupyter Notebook

```bash
jupyter notebook notebooks/eda_notebook.ipynb
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📷 Dashboard Preview

## Dashboard Home

<img width="1915" height="912" src="https://github.com/user-attachments/assets/41d88548-f7ed-4f6c-9fe1-aee7f441f73b"/>

---

## Interactive Analytics

<img width="1917" height="911" src="https://github.com/user-attachments/assets/b3ecb5c5-abbd-482d-a72f-c7ac4c8bb8de"/>

---

> Additional visualizations and dashboard screenshots will be added in future updates.

---

# 📈 Key Insights

- Jeff Kinney, Rick Riordan, and Suzanne Collins consistently appear among the most successful bestselling authors.
- Fiction books generally receive more customer reviews than Non-Fiction books.
- Customer engagement increased significantly between 2009 and 2019.
- Average book prices gradually decreased over the decade.
- Price shows little to no meaningful relationship with user ratings.

Detailed findings are available in:

```
reports/business_insights.md
```

---

# 🛣 Development Roadmap

## ✅ Version 1.0

- Data Cleaning
- EDA
- Interactive Dashboard
- Business Report

---

## 🚀 Version 1.1

- Dashboard UI Improvements
- Additional KPIs
- Enhanced Filtering
- Improved Visualizations

---

## 🔮 Version 2.0

- Machine Learning Recommendations
- Sentiment Analysis
- Book Popularity Prediction
- Live Dataset Integration
- Dashboard Deployment

---

# 💡 Future Scope

- NLP-based Review Sentiment Analysis
- Recommendation System
- Genre Popularity Forecasting
- Machine Learning Models
- Live Amazon Bestseller Tracking
- Cloud Deployment

---

# 📚 What I Learned

This project strengthened my understanding of:

- Data preprocessing
- Exploratory data analysis
- Statistical interpretation
- Dashboard development
- Data visualization
- Python best practices
- Converting raw data into actionable business insights

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to:

- Fork the repository
- Create a feature branch
- Commit your improvements
- Submit a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

## **Keerthana K R**

**Aspiring Software Engineer | Python Full Stack Developer**

Passionate about building data-driven applications using Python, Django, SQL, and modern analytics tools while continuously improving software engineering skills through real-world projects.

⭐ **If you found this project helpful, consider giving it a Star on GitHub!**
