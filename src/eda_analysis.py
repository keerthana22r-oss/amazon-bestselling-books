"""
eda_analysis.py

All exploratory analysis and chart-generation logic, kept separate from
notebooks so the same functions can be reused by the Streamlit dashboard.

Design decision: every function returns a matplotlib Figure object rather
than calling plt.show(). This makes functions testable and reusable in
different contexts (notebook display, saving to file, or embedding in
Streamlit via st.pyplot(fig)) instead of being tied to one output method.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

plt.style.use("seaborn-v0_8-whitegrid")


# ---------- AUTHOR ANALYSIS ----------

def top_authors_by_book_count(df: pd.DataFrame, n: int = 10):
    """Bar chart: which authors appear most often as bestsellers."""
    counts = df["author"].value_counts().head(n)
    fig, ax = plt.subplots(figsize=(9, 5))
    counts.sort_values().plot(kind="barh", ax=ax, color="#4C72B0")
    ax.set_title(f"Top {n} Authors by Number of Bestselling Books")
    ax.set_xlabel("Number of Bestselling Books")
    ax.set_ylabel("Author")
    fig.tight_layout()
    return fig


def highest_rated_authors(df: pd.DataFrame, n: int = 10, min_books: int = 2):
    """
    Bar chart: authors with the highest average rating.

    min_books filters out one-hit authors, since an author with a single
    4.9-rated book isn't meaningfully 'higher rated' than one who
    consistently rates 4.7 across five books. This avoids a small-sample
    bias that would otherwise dominate the top of the list.
    """
    grouped = df.groupby("author").agg(
        avg_rating=("user_rating", "mean"),
        book_count=("name", "count")
    )
    grouped = grouped[grouped["book_count"] >= min_books]
    top = grouped.sort_values("avg_rating", ascending=False).head(n)

    fig, ax = plt.subplots(figsize=(9, 5))
    top["avg_rating"].sort_values().plot(kind="barh", ax=ax, color="#55A868")
    ax.set_title(f"Top {n} Highest-Rated Authors (min. {min_books} books)")
    ax.set_xlabel("Average User Rating")
    ax.set_ylabel("Author")
    ax.set_xlim(4.0, 5.0)
    fig.tight_layout()
    return fig


def most_reviewed_authors(df: pd.DataFrame, n: int = 10):
    """Bar chart: authors whose books collectively drew the most reviews."""
    grouped = df.groupby("author")["reviews"].sum().sort_values(ascending=False).head(n)
    fig, ax = plt.subplots(figsize=(9, 5))
    grouped.sort_values().plot(kind="barh", ax=ax, color="#C44E52")
    ax.set_title(f"Top {n} Most-Reviewed Authors (Total Reviews)")
    ax.set_xlabel("Total Reviews")
    ax.set_ylabel("Author")
    ax.xaxis.set_major_formatter(mticker.StrMethodFormatter("{x:,.0f}"))
    fig.tight_layout()
    return fig


# ---------- BOOK ANALYSIS ----------

def rating_distribution(df: pd.DataFrame):
    """Histogram: how ratings are distributed across all bestsellers."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["user_rating"], bins=12, color="#8172B2", edgecolor="white")
    ax.set_title("Distribution of User Ratings Across Bestsellers")
    ax.set_xlabel("User Rating")
    ax.set_ylabel("Number of Books")
    fig.tight_layout()
    return fig


def price_extremes(df: pd.DataFrame, n: int = 5):
    """Returns (most_expensive, least_expensive) DataFrames, not a chart."""
    most_expensive = df.nlargest(n, "price")[["name", "author", "price", "year"]]
    least_expensive = df.nsmallest(n, "price")[["name", "author", "price", "year"]]
    return most_expensive, least_expensive


# ---------- GENRE ANALYSIS ----------

def genre_comparison(df: pd.DataFrame):
    """
    Grouped bar chart comparing avg rating and avg price by genre.

    Two separate y-scales matter here: rating (3.3-4.9) and price ($0-105)
    are on wildly different scales, so we use two subplots side by side
    rather than forcing them onto one shared axis, which would make the
    rating bars invisible next to price bars.
    """
    grouped = df.groupby("genre").agg(
        avg_rating=("user_rating", "mean"),
        avg_price=("price", "mean"),
        avg_reviews=("reviews", "mean"),
        count=("name", "count")
    )

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    grouped["avg_rating"].plot(kind="bar", ax=axes[0], color=["#4C72B0", "#DD8452"])
    axes[0].set_title("Avg Rating by Genre")
    axes[0].set_ylim(4.0, 5.0)
    axes[0].set_xlabel("")
    axes[0].tick_params(axis="x", rotation=0)

    grouped["avg_price"].plot(kind="bar", ax=axes[1], color=["#4C72B0", "#DD8452"])
    axes[1].set_title("Avg Price by Genre ($)")
    axes[1].set_xlabel("")
    axes[1].tick_params(axis="x", rotation=0)

    grouped["avg_reviews"].plot(kind="bar", ax=axes[2], color=["#4C72B0", "#DD8452"])
    axes[2].set_title("Avg Reviews by Genre")
    axes[2].set_xlabel("")
    axes[2].tick_params(axis="x", rotation=0)
    axes[2].yaxis.set_major_formatter(mticker.StrMethodFormatter("{x:,.0f}"))

    fig.tight_layout()
    return fig, grouped


def genre_share_pie(df: pd.DataFrame):
    """Pie chart: proportion of Fiction vs Non Fiction bestsellers."""
    counts = df["genre"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%",
           colors=["#4C72B0", "#DD8452"], startangle=90)
    ax.set_title("Share of Bestsellers: Fiction vs Non Fiction")
    fig.tight_layout()
    return fig


# ---------- YEAR ANALYSIS ----------

def yearly_trends(df: pd.DataFrame):
    """
    Line charts: how avg rating, avg reviews, and avg price moved 2009-2019.

    Note: 'books released each year' is a constant 50 (fixed dataset design,
    Amazon's Top 50 list), so that's reported as a fact rather than charted
    as a trend line, which would just be a flat line at y=50 and add no
    insight.
    """
    yearly = df.groupby("year").agg(
        avg_rating=("user_rating", "mean"),
        avg_reviews=("reviews", "mean"),
        avg_price=("price", "mean"),
        book_count=("name", "count")
    )

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    axes[0].plot(yearly.index, yearly["avg_rating"], marker="o", color="#4C72B0")
    axes[0].set_title("Avg Rating by Year")
    axes[0].set_xlabel("Year")

    axes[1].plot(yearly.index, yearly["avg_reviews"], marker="o", color="#55A868")
    axes[1].set_title("Avg Reviews by Year")
    axes[1].set_xlabel("Year")
    axes[1].yaxis.set_major_formatter(mticker.StrMethodFormatter("{x:,.0f}"))

    axes[2].plot(yearly.index, yearly["avg_price"], marker="o", color="#C44E52")
    axes[2].set_title("Avg Price by Year")
    axes[2].set_xlabel("Year")

    fig.tight_layout()
    return fig, yearly


# ---------- CORRELATION ANALYSIS ----------

def correlation_heatmap(df: pd.DataFrame):
    """
    Heatmap of correlations between rating, reviews, and price.

    Business question this answers: does a higher price correlate with
    higher quality (rating)? Do more-reviewed books rate higher (social
    proof) or is that independent? Correlation alone doesn't prove
    causation, which is a nuance worth stating explicitly in interviews.
    """
    corr = df[["user_rating", "reviews", "price"]].corr()

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr.columns)
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="black")
    ax.set_title("Correlation Heatmap: Rating, Reviews, Price")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    return fig, corr


def price_vs_rating_scatter(df: pd.DataFrame):
    """Scatter plot: does price relate to rating at the individual book level?"""
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = df["genre"].map({"Fiction": "#4C72B0", "Non Fiction": "#DD8452"})
    ax.scatter(df["price"], df["user_rating"], c=colors, alpha=0.6, edgecolor="white")
    ax.set_title("Price vs. Rating (colored by Genre)")
    ax.set_xlabel("Price ($)")
    ax.set_ylabel("User Rating")
    fig.tight_layout()
    return fig


def rating_boxplot_by_genre(df: pd.DataFrame):
    """Box plot: rating spread and outliers per genre."""
    fig, ax = plt.subplots(figsize=(7, 5))
    df.boxplot(column="user_rating", by="genre", ax=ax,
               patch_artist=True,
               boxprops=dict(facecolor="#8172B2"))
    ax.set_title("Rating Spread by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("User Rating")
    fig.suptitle("")
    fig.tight_layout()
    return fig
