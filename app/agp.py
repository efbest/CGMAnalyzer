import numpy as np
import pandas as pd

def compute_agp(df):
    """
    Groups glucose values by time of day and computes AGP statistics.
    Returns a DataFrame with time, p10, q1, median, q3, p90.
    """
    if "timestamp" not in df.columns or "glucose" not in df.columns:
        raise ValueError("DataFrame must contain 'timestamp' and 'glucose' columns.")

    df = df.copy()
    df["minutes_since_midnight"] = df["timestamp"].dt.hour * 60 + df["timestamp"].dt.minute

    agp = df.groupby("minutes_since_midnight")["glucose"].agg([
        ("p10", lambda x: np.percentile(x, 10)),
        ("q1", lambda x: np.percentile(x, 25)),
        ("median", "median"),
        ("q3", lambda x: np.percentile(x, 75)),
        ("p90", lambda x: np.percentile(x, 90)),
    ]).reset_index()

    agp["time"] = pd.to_timedelta(agp["minutes_since_midnight"], unit="m")
    return agp
