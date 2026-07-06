"""
app.py — Streamlit dashboard for the Amazon Best Selling Books dataset.

Design decisions:
- Imports cleaning/analysis logic from src/, no duplicated logic here.
- Uses st.cache_data so the (small) dataset isn't re-loaded/re-cleaned on
  every widget interaction, which would slow the app down noticeably.
- Filters are applied to a single working dataframe that feeds every KPI,
  chart, and the download button, so everything stays in sync.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd

from src.data_cleaning import load_raw_data, clean_dataset
from src import eda_analysis as eda

st.set_page_config(
    page_title="Amazon Bestselling Books Dashboard",
    page_icon="📚",
    layout="wide",
)


@st.cache_data
def get_data():
    raw = load_raw_data("data/raw/bestsellers_with_categories.csv")
    return clean_dataset(raw)


df = get_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

search_title = st.sidebar.text_input("Search by book title")
search_author = st.sidebar.text_input("Search by author")

genres = st.sidebar.multiselect(
    "Genre", options=sorted(df["genre"].unique()), default=list(df["genre"].unique())
)

year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.sidebar.slider("Year range", year_min, year_max, (year_min, year_max))

price_min, price_max = int(df["price"].min()), int(df["price"].max())
price_range = st.sidebar.slider("Price range ($)", price_min, price_max, (price_min, price_max))

rating_min, rating_max = float(df["user_rating"].min()), float(df["user_rating"].max())
rating_range = st.sidebar.slider(
    "Rating range", rating_min, rating_max, (rating_min, rating_max), step=0.1
)

# ---------------- APPLY FILTERS ----------------
filtered = df.copy()

if search_title:
    filtered = filtered[filtered["name"].str.contains(search_title, case=False, na=False)]

if search_author:
    filtered = filtered[filtered["author"].str.contains(search_author, case=False, na=False)]

filtered = filtered[filtered["genre"].isin(genres)]
filtered = filtered[filtered["year"].between(*year_range)]
filtered = filtered[filtered["price"].between(*price_range)]
filtered = filtered[filtered["user_rating"].between(*rating_range)]

# ---------------- HEADER ----------------
st.title("📚 Amazon Best Selling Books Dashboard (2009–2019)")
st.caption("Explore 10 years of Amazon's Top 50 Bestselling Books — filter, search, and download.")

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Books shown", f"{len(filtered):,}")
col2.metric("Avg rating", f"{filtered['user_rating'].mean():.2f}" if len(filtered) else "—")
col3.metric("Avg price", f"${filtered['price'].mean():.2f}" if len(filtered) else "—")
col4.metric("Total reviews", f"{filtered['reviews'].sum():,}" if len(filtered) else "—")

st.divider()

if filtered.empty:
    st.warning("No books match the current filters. Try widening your filter selection.")
    st.stop()

# ---------------- TABS FOR CHARTS ----------------
tab1, tab2, tab3, tab4 = st.tabs(["Authors", "Genre", "Year Trends", "Correlation"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.pyplot(eda.top_authors_by_book_count(filtered))
    with c2:
        st.pyplot(eda.most_reviewed_authors(filtered))
    st.pyplot(eda.highest_rated_authors(filtered, min_books=1))

with tab2:
    fig_genre, genre_stats = eda.genre_comparison(filtered)
    st.pyplot(fig_genre)
    c1, c2 = st.columns(2)
    with c1:
        st.pyplot(eda.genre_share_pie(filtered))
    with c2:
        st.dataframe(genre_stats.style.format({"avg_rating": "{:.2f}", "avg_price": "${:.2f}", "avg_reviews": "{:,.0f}"}))

with tab3:
    fig_year, year_stats = eda.yearly_trends(filtered)
    st.pyplot(fig_year)
    st.dataframe(year_stats)

with tab4:
    fig_corr, corr = eda.correlation_heatmap(filtered)
    c1, c2 = st.columns(2)
    with c1:
        st.pyplot(fig_corr)
    with c2:
        st.pyplot(eda.price_vs_rating_scatter(filtered))

st.divider()

# ---------------- DATA TABLE + DOWNLOAD ----------------
st.subheader("Filtered Data")
st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download filtered data as CSV",
    data=csv_data,
    file_name="filtered_bestsellers.csv",
    mime="text/csv",
)
