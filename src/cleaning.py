"""Data cleaning utilities for the churn prediction project."""


def clean_retail_data(df):
    """Clean raw online retail data.

    Responsibilities include:
    - dropping rows without CustomerID
    - handling cancelled invoices (C)
    - removing duplicates and invalid prices/quantities
    - standardizing datetime fields
    """
    raise NotImplementedError("Implement cleaning logic here.")

