import pandas as pd
import io

def load_and_parse_file(uploaded_file):
    try:
        content = uploaded_file.read().decode("utf-8", errors="ignore")
        if "Glukosewert-Verlauf" in content:
            return parse_libreview(uploaded_file), "Freestyle Libre"
        elif "Ereignisart" in content and "EGV" in content:
            return parse_dexcom(uploaded_file), "Dexcom Clarity"
        else:
            return None, "Unknown format"
    except Exception as e:
        return None, f"Parsing error: {e}"

def parse_libreview(uploaded_file):
    df = pd.read_csv(uploaded_file, header=2)
    df = df.rename(columns={
        "Gerätezeitstempel": "timestamp",
        "Glukosewert-Verlauf mg/dL": "glucose"
    })
    df["timestamp"] = pd.to_datetime(df["timestamp"], dayfirst=True, errors="coerce")
    df["glucose"] = pd.to_numeric(df["glucose"], errors="coerce")
    df = df.dropna(subset=["timestamp", "glucose"])
    df = df[(df["glucose"] >= 40) & (df["glucose"] <= 400)]
    return df.sort_values("timestamp")

def parse_dexcom(uploaded_file):
    df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8")
    df = df[df["Ereignisart"] == "EGV"]
    df = df.rename(columns={
        "Zeitstempel (JJJJ-MM-TTThh:mm:ss)": "timestamp",
        "Glukosewert (mg/dl)": "glucose"
    })
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["glucose"] = pd.to_numeric(df["glucose"], errors="coerce")
    df = df.dropna(subset=["timestamp", "glucose"])
    df = df[(df["glucose"] >= 40) & (df["glucose"] <= 400)]
    return df.sort_values("timestamp")
