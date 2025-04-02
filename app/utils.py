import pandas as pd

def convert_mmol_to_mgdl(df, column="glucose"):
    """Convert mmol/L to mg/dL in-place."""
    df[column] = df[column] * 18.0
    return df

def normalize_timestamps(df, column="timestamp"):
    """Ensure timestamp column is timezone-naive and properly formatted."""
    df[column] = pd.to_datetime(df[column], errors="coerce")
    df = df.dropna(subset=[column])
    df[column] = df[column].dt.tz_localize(None)
    return df

def round_time_to_nearest_minute(df, column="timestamp"):
    """Round timestamp column to the nearest minute."""
    df[column] = df[column].dt.round("1min")
    return df
