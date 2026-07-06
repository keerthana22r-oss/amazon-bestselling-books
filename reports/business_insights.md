# Business Insights — Amazon Best Selling Books (2009–2019)

This report summarizes the key, data-backed findings from the analysis in
`notebooks/eda_notebook.ipynb`.

## 1. Top-Performing Authors

Series/franchise authors dominate bestseller frequency:
**Jeff Kinney (12 book-years), Suzanne Collins (11), Rick Riordan (11),
Gary Chapman (11)**. This suggests that appearing repeatedly on the
bestseller list is often driven by an established series or franchise
audience, not necessarily by any single standout title. **Implication for
publishers:** investing in a strong existing franchise carries more
predictable bestseller odds than betting on a single new release.

## 2. Genre Trends

- Fiction titles average a slightly higher rating (**4.65 vs 4.60**) and
  draw substantially more reviews per book (**~15,684 vs ~9,065**) than
  Non Fiction.
- Non Fiction is priced higher on average (**~$14.84 vs ~$10.85**) despite
  drawing fewer reviews — consistent with Non Fiction's positioning as
  reference/premium content rather than mass entertainment.
- **Implication:** Fiction appears to have a more actively engaged reader
  base (higher review volume per book), while Non Fiction commands a
  price premium without a proportional engagement boost.

## 3. Pricing Patterns

- Average price **declined from ~$15.40 (2009) to ~$10.08 (2019)** —
  consistent with the broader e-book/Kindle pricing deflation trend across
  the decade.
- Price shows **no meaningful correlation with rating** (correlation
  coefficient: **-0.13**). Higher-priced books are not reliably
  better-rated. **Implication:** price is a poor proxy for quality in this
  market — consumers are not reliably paying more for better-rated books.
- A small number of $0-priced titles were confirmed as genuine
  promotional/public-domain listings (e.g. *To Kill a Mockingbird* during
  a known Kindle giveaway period), not missing data.

## 4. Rating Patterns

- Ratings cluster heavily between **4.5 and 4.9** — expected, since
  bestseller lists are inherently rating-biased (poorly-rated books rarely
  reach bestseller status in the first place).
- Rating shows **negligible correlation with review count** (**-0.002**).
  A heavily-reviewed book is not reliably a higher-rated one — review
  volume reflects reach/popularity, not necessarily satisfaction.

## 5. Customer Review Behavior

Average reviews per book **more than tripled over the decade**, from
**~4,710 (2009) to ~15,898 (2019)**. This most plausibly reflects Amazon's
overall platform growth and an increasing review-leaving culture over time,
rather than a change in book quality itself — a distinction worth stating
explicitly rather than over-interpreting the trend as "books got better."

## 6. Year-over-Year Observations

| Year | Avg Rating | Avg Reviews | Avg Price |
|------|-----------|-------------|-----------|
| 2009 | 4.58 | ~4,710 | $15.40 |
| 2019 | 4.74 | ~15,898 | $10.08 |

All three metrics moved in the reader-favorable direction over the decade:
ratings up modestly, reviews up substantially, and prices down.

## Key Caveat

Correlation values throughout this analysis are weak (all under 0.15 in
magnitude). This means **no strong linear relationship** was found between
price, reviews, and rating — it does not prove these variables are
completely unrelated, only that no strong linear pattern exists in this
550-row sample. This distinction is important to state precisely rather
than overclaiming causation or independence.
