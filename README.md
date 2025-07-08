# Netflix Data Analysis

This project explores the Netflix dataset consisting of 8,804 rows and 12 columns. It contains details like title, cast, release year, directors, genres, country of origin, duration, and type (Movie or TV Show).

---

## Key Insights

- Top 10 countries by number of Netflix titles
- Distribution of genres across the platform
- Country-wise content production trends
- Most frequently appearing actors and directors
- Proportion of Movies vs. TV Shows on Netflix

---

## Tools Used

- Python: `pandas`, `seaborn`, `matplotlib`,`plotly`
- Jupyter Notebook

---

## What I Learned

- How to handle missing values smartly: Instead of dropping crucial columns like `cast`, `director`, or `country`, I replaced missing entries with `'Unknown'` so they could still be visualized meaningfully.
- Learned when to use different types of plots like bar plots vs. histograms.
- Discovered and applied new pandas operations like `explode()` and `reset_index()` for simplifying data transformations.
- Practiced real-world data cleaning techniques — especially with parsing and restructuring actor/director data for analysis.
- While some earlier years (pre-1960s) had very few entries and were flagged as statistical outliers, they represent older classic titles and were retained for historical completeness.
---

## Dataset

- [Netflix Movies and TV Shows Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## How to Run

1. Clone or download the repository.
2. Open `Netflix.ipynb` using Jupyter Notebook.
3. Run all cells to see the analysis and visualizations.

---

😉 This project was built with a focus on storytelling through data, and preparing for real-world analytics tasks like those at Netflix.
