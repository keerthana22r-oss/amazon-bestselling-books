"""
data_cleaning.py

Reusable functions for loading and cleaning the Amazon Best Selling Books dataset.
Kept separate from notebooks so the same logic can be imported into
EDA notebooks AND the Streamlit dashboard without duplication.
"""

import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """Load the raw CSV exactly as downloaded from Kaggle."""
    return pd.read_csv(path)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to snake_case.

    Why: 'User Rating' with a space requires bracket access (df['User Rating'])
    everywhere in code. Snake_case columns (df.user_rating) are easier to type,
    less error-prone, and match Python/pandas convention.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all cleaning steps to the raw dataframe.

    Steps:
    1. Rename columns to snake_case.
    2. Remove fully duplicate rows (exact copies) — none found in raw data,
       but this guards against future re-runs on updated/re-scraped data.
    3. Standardize 'genre' text casing/whitespace.
    4. Ensure dtypes are correct (rating=float, reviews/price/year=int).

    Note: rows where price == 0 are intentionally NOT modified. Investigation
    showed these are genuine promotional/free listings (e.g. public domain
    titles, Kindle giveaways), not missing data placeholders.

    Note: repeated book titles across different years are intentionally NOT
    treated as duplicates — a book can legitimately be a bestseller in
    multiple years, and each year is a distinct, meaningful record.
    """
    df = clean_column_names(df)

    # Step 2: remove exact duplicate rows (defensive — none exist currently)
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    # Step 3: standardize genre text
    df["genre"] = df["genre"].str.strip().str.title()

    # Step 4: enforce dtypes explicitly (defensive against future re-scrapes
    # where a numeric column might get read in as text due to stray characters)
    df["user_rating"] = df["user_rating"].astype(float)
    df["reviews"] = df["reviews"].astype(int)
    df["price"] = df["price"].astype(int)
    df["year"] = df["year"].astype(int)

    if removed > 0:
        print(f"Removed {removed} exact duplicate row(s).")

    return df


if __name__ == "__main__":
    raw = load_raw_data("data/raw/bestsellers_with_categories.csv")
    cleaned = clean_dataset(raw)
    cleaned.to_csv("data/processed/bestsellers_clean.csv", index=False)
    print(f"Cleaned dataset saved: {cleaned.shape[0]} rows, {cleaned.shape[1]} columns.")
