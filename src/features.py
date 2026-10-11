"""Feature engineering and RFM segmentation utilities."""


def build_churn_features(df, cutoff_date):
    """Create churn labels and derived customer-level features."""
    raise NotImplementedError("Implement feature engineering here.")


def create_rfm_segments(df):
    """Assign RFM segments based on recency, frequency, and monetary value."""
    raise NotImplementedError("Implement RFM segmentation here.")

