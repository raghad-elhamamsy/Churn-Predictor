# Customer Churn Predictor with RFM Segmentation

A machine learning project that identifies customers at risk of churning in an online retail business. The solution combines customer segmentation, time-based feature engineering, and explainable ML to support marketing and retention decisions.

## Project idea

This project uses the online retail dataset to build a customer churn prediction system. The goal is to detect customers likely to stop buying and explain why they are at risk, so business teams can act before revenue drops.

### Churn definition
- Cutoff date: 30-09-2011
- Only customers active before the cutoff are included
- A customer is labeled as churned if they made no purchases between 01-10-2011 and the end of the dataset (about 70 days)
- Features are built only from purchases before the cutoff to avoid leakage

### Business value
- Customer lookup: enter a CustomerID and view churn probability, risk level, segment, and top SHAP-based reasons
- Segment dashboard: compare churn rates by RFM segment and suggest next actions
- Batch scoring: upload a CSV and download churn predictions for many customers

## Repo structure

```text
churn-predictor/
├── data/                     # raw data (not committed; add dataset link in README)
│   └── .gitkeep
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_features.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── features.py
│   ├── train.py
│   └── predict.py
├── models/
│   └── .gitkeep
├── app/
│   └── app.py
├── slides/
│   └── .gitkeep
├── .gitignore
├── requirements.txt
├── README.md
└── .env.example             # optional, if you add API keys or local config later
```

## Workflow

1. Clean the raw online retail data
   - drop rows without CustomerID
   - handle cancelled invoices (invoice codes starting with C)
   - remove duplicate records and invalid prices/quantities

2. Perform exploratory data analysis (EDA)
   - study purchase behavior, missingness, and monetary distribution
   - derive RFM variables and segment insights

3. Define churn label and create time-based features
   - build features from transactions before the cutoff date
   - time-split the dataset to avoid leakage

4. Train and compare models
   - baseline model
   - logistic regression
   - random forest
   - XGBoost or LightGBM
   - evaluate using precision, recall, F1, and PR-AUC

5. Add explainability
   - use SHAP values to explain the top reasons a customer may churn

6. Build the Streamlit app
   - customer lookup
   - segment overview dashboard
   - batch upload and scoring workflow

7. Finalize documentation and presentation
   - README
   - slides
   - LinkedIn post and workday summary

## Data source

The project is based on the Online Retail dataset, which is typically available from the UCI Machine Learning Repository or a public Kaggle mirror.

Suggested data handling:
- store raw data in `data/`
- do not commit the dataset to GitHub
- document the data source and version in the project notes

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/churn-predictor.git
cd churn-predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app/app.py
```

## Team roles and responsibilities

| Member | Role | Owns | Hands off |
|---|---|---|---|
| 1 | Data & EDA | Cleaning, EDA, RFM segmentation, segment insights | cleaned dataset |
| 2 | Features & labeling | Churn definition, time-based split, feature engineering | feature dataset |
| 3 | Modeling | Baseline, models, tuning, metrics, SHAP | model artifact and metrics |
| 4 | App & repo | Streamlit app, README, repo structure, integration | working app and repo |

This repo structure is designed so each team member can work in parallel while keeping a clear handoff process.

## Evaluation strategy

Model performance should be assessed with business-relevant metrics, especially:
- precision
- recall
- F1-score
- PR-AUC

These metrics are useful because churn prediction usually deals with imbalanced classes, and the business goal is often to identify the highest-value at-risk customers with a strong recall and controlled false positives.

## Notes

- Do not commit sensitive or large data files
- Save the trained model and evaluation metrics in `models/`
- Keep notebooks organized by task (EDA, feature engineering, and modeling)
- Keep the app logic simple and production-friendly for demonstration and deployment

## Future improvements

- add automated retraining pipelines
- deploy the model via a cloud platform
- build monitoring for drift and data quality
- add customer-level cohort analyses and retention recommendations

## License

This project is intended for educational and portfolio use. Add a license file if you plan to publish it publicly.
