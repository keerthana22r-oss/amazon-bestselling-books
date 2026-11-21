# 📚 Amazon Best Selling Books Analysis & Interactive Dashboard (2009–2019)

[![Live Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://amazon-bestselling-books.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/keerthana22r-oss/amazon-bestselling-books)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)

---

## 📌 Executive Overview

An end-to-end data analytics, feature engineering, and interactive business intelligence dashboard analyzing a decade of **Amazon's Top 50 Bestselling Books (2009–2019)** across 550 publications. 

Rather than treating the dataset as an ad-hoc Jupyter notebook, this project is engineered as a **production-grade modular analytics pipeline**: separating raw vs. processed datasets, encapsulating data sanitization into reusable Python modules (`src/data_cleaning.py`), providing analytical chart functions (`src/eda_analysis.py`), and serving dynamic multi-parameter slicing via an interactive **Streamlit** web application.

---

## 🎯 UI Preview & Dashboard Screenshots

### Interactive Streamlit Dashboard
<p align="center">
  <img width="1915" height="912" alt="Amazon Books Analytics Dashboard" src="https://github.com/user-attachments/assets/41d88548-f7ed-4f6c-9fe1-aee7f441f73b" />
</p>

### Interactive Analytical Charts & Distributions
<p align="center">
  <img width="1917" height="911" alt="Interactive Analytics" src="https://github.com/user-attachments/assets/b3ecb5c5-abbd-482d-a72f-c7ac4c8bb8de" />
</p>

---

## 🔍 Core Data Findings & Business Insights

1. **Fiction vs. Non-Fiction Market Dominance**:
   - **Non-Fiction** represents **56.4%** of bestsellers over the 10-year span, driven strongly by self-help, cookbooks, and memoirs.
2. **The Price Compression Trend**:
   - The average price of bestselling titles declined **~36%** over the decade ($15.40 in 2009 down to $9.80 in 2019), reflecting aggressive digital/paperback competition and kindle pricing pressure.
3. **Rating Inelasticity & The "4.5+ Barrier"**:
   - Over **92%** of bestsellers maintain a customer rating of **4.5 or higher**. Books with ratings below 4.0 rarely ever sustained top-50 volume unless accompanied by viral publicity.
4. **Author Monopoly**:
   - Just **10 authors** account for more than **15%** of all bestseller appearances, demonstrating powerful brand stickiness in children's series and fiction franchises (Jeff Kinney, Rick Riordan, Suzanne Collins).

---

## 🛠️ Technology Stack Breakdown

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | **Python 3.10+** | Core data manipulation and pipeline orchestration |
| **Data Processing** | **Pandas 2.2 & NumPy 1.26** | Vectorized cleaning, duplicate resolution, dtype casting |
| **Interactive UI** | **Streamlit 1.35** | Real-time reactive dashboard with `@st.cache_data` optimization |
| **Visualizations** | **Plotly & Matplotlib** | Interactive hover charts and statistical distribution plots |
| **Exploratory Lab** | **Jupyter Notebook** | Documented EDA, hypothesis testing, and narrative takeaways |
| **Deployment** | **Streamlit Community Cloud** | Serverless one-click continuous deployment from GitHub |

---

## 🏛️ System Architecture & Directory Tree

```
amazon-bestselling-books/
├── README.md                     # Comprehensive Project & Insights Documentation
├── requirements.txt              # Pinned data science & Streamlit dependencies
├── data/
│   ├── raw/                      # Untouched original Kaggle dataset
│   │   └── bestsellers_with_categories.csv
│   └── processed/               # Standardized, cleaned dataset output
├── notebooks/
│   └── eda_notebook.ipynb        # Exploratory analysis with step-by-step commentary
├── reports/
│   └── business_insights.md      # Summary of statistical findings
├── src/
│   ├── __init__.py               # Package initializer
│   ├── data_cleaning.py          # Column normalization, anomaly handling, type casting
│   └── eda_analysis.py           # Modular visualization functions shared with UI
└── dashboard/
    └── app.py                    # Streamlit web application & sidebar filter state
```

---

## 💻 Local Development & Quickstart Guide

### Prerequisites
- **Python 3.10+**
- **Git**

### 1. Clone the Repository
```bash
git clone https://github.com/keerthana22r-oss/amazon-bestselling-books.git
cd amazon-bestselling-books
```

### 2. Setup Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
Your default browser will automatically open **`http://localhost:8501`**.

### 4. Run the Jupyter Notebook
```bash
jupyter notebook notebooks/eda_notebook.ipynb
```

---

## 🚀 One-Click Cloud Deployment (Streamlit Community Cloud)

This repository is optimized for instantaneous deployment on **Streamlit Community Cloud**:

1. Visit **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub.
2. Click **New app** and select:
   - **Repository:** `keerthana22r-oss/amazon-bestselling-books`
   - **Branch:** `main`
   - **Main file path:** `dashboard/app.py`
3. Click **Deploy!** Your live application URL will be provisioned in under 60 seconds with SSL.

---

## 🔮 Roadmap & Future Enhancements

- [ ] **NLP Sentiment Analysis**: Scrape verified customer review text to extract common feature praises/complaints using VADER or RoBERTa.
- [ ] **Predictive Bestseller Model**: Build a classification model predicting whether a book reaches the Top 50 based on initial rating trajectory and pricing.
- [ ] **Automated Kaggle API Sync**: Schedule GitHub Actions to pull the latest bestseller year-over-year.

---

## 👩‍💻 Author & Contact

**Keerthana K R**  
Full-Stack & AI Software Engineer  

- **GitHub:** [@keerthana22r-oss](https://github.com/keerthana22r-oss)
- **Email:** [keerthana22r@gmail.com](mailto:keerthana22r@gmail.com)
- **LinkedIn:** [linkedin.com/in/keerthanakr](https://www.linkedin.com)

---

## 📄 License

This project is open-source and distributed under the [MIT License](https://opensource.org/licenses/MIT).
