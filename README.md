# 📚 Amazon Best Selling Books Analysis (2009–2019)

An end-to-end data analytics project analyzing a decade of Amazon's Top 50
Bestselling Books — covering data cleaning, exploratory data analysis,
visualization, and an interactive Streamlit dashboard.

## Project Overview

This project takes a raw, real-world dataset of 550 bestselling books and
walks it through a complete analytics pipeline: data quality investigation,
cleaning with documented reasoning, exploratory analysis across authors,
genres, years, and correlations, and a filterable interactive dashboard for
exploring the data live.


## Features

- **Documented, reusable cleaning pipeline** (`src/data_cleaning.py`) —
  handles column standardization, dtype enforcement, and duplicate checks,
  with explicit reasoning for anomalies (e.g. $0-priced books) rather than
  blind imputation.
- **Modular EDA library** (`src/eda_analysis.py`) — every chart is a
  reusable function shared between the Jupyter notebook and the dashboard.
- **Interactive Streamlit dashboard** — KPI cards, search by title/author,
  genre/year/price/rating filters, and CSV export of filtered results.
- **Business insights report** grounded entirely in the data, with explicit
  caveats about correlation vs. causation.

## Technologies Used

- **Python 3** — core language
- **Pandas / NumPy** — data manipulation
- **Matplotlib** — static visualizations
- **Streamlit** — interactive dashboard
- **Jupyter Notebook** — exploratory analysis
- **Git & GitHub** — version control

## Dataset

[Amazon Top 50 Bestselling Books 2009-2019](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019)
(Kaggle, by sootersaalu) — 550 rows, 7 columns:

| Column | Description |
|---|---|
| Name | Book title |
| Author | Book's author |
| User Rating | Average Amazon rating (3.3–4.9) |
| Reviews | Number of customer reviews |
| Price | Price in USD |
| Year | Bestseller year (2009–2019) |
| Genre | Fiction / Non Fiction |

## Project Structure

```
amazon-bestselling-books/
├── data/
│   ├── raw/                  # Original, untouched dataset
│   └── processed/            # Cleaned dataset
├── notebooks/
│   └── eda_notebook.ipynb    # Full exploratory analysis with insights
├── src/
│   ├── data_cleaning.py      # Reusable cleaning functions
│   └── eda_analysis.py       # Reusable chart-generating functions
├── dashboard/
│   └── app.py                # Streamlit dashboard
├── images/                   # Exported chart images
├── reports/
│   └── business_insights.md  # Written business findings
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <your-repo-url>
cd amazon-bestselling-books
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

**Run the EDA notebook:**
```bash
jupyter notebook notebooks/eda_notebook.ipynb
```

**Run the dashboard locally:**
```bash
streamlit run dashboard/app.py
```

## Dashboard Preview

<img width="1915" height="912" alt="image" src="https://github.com/user-attachments/assets/41d88548-f7ed-4f6c-9fe1-aee7f441f73b" />
<img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/b3ecb5c5-abbd-482d-a72f-c7ac4c8bb8de" />



`![Dashboard preview](images/genre_comparison.png)`

## Key Insights

- Series/franchise authors (Jeff Kinney, Suzanne Collins, Rick Riordan)
  dominate bestseller frequency.
- Fiction rates slightly higher and draws far more reviews than Non
  Fiction, despite being priced lower on average.
- Average reviews per book roughly tripled from 2009 to 2019.
- Average price declined over the same period.
- Price and review count show **no meaningful correlation** with rating.

Full findings: [`reports/business_insights.md`](reports/business_insights.md)

## Future Improvements

- Add sentiment analysis on review text (would require a richer dataset
  with review content, not just counts).
- Deploy with a scheduled data refresh if a live Amazon bestseller feed
  becomes available.
- Add author-level drill-down pages to the dashboard.

## License

MIT
