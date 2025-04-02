import numpy as np

def compute_metrics(df):
    glucose = df["glucose"]
    stats = {
        "Mean Glucose (mg/dL)": round(glucose.mean(), 1),
        "Standard Deviation": round(glucose.std(), 1),
        "Coefficient of Variation (%)": round((glucose.std() / glucose.mean()) * 100, 1),
        "TIR (70–180 mg/dL)": round(((glucose >= 70) & (glucose <= 180)).mean() * 100, 1),
        "Low (<70 mg/dL)": round((glucose < 70).mean() * 100, 1),
        "High (>180 mg/dL)": round((glucose > 180).mean() * 100, 1),
    }
    return stats
