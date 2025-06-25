import pandas as pd

# === Parameter für Anomaliegrenzen ===
TEMP_THRESHOLD = 80     # Temperaturgrenze (°C)
VIB_THRESHOLD = 0.04    # Vibrationsgrenze

def detect_anomalies(df):
    """
    Regelbasierte Anomalie-Erkennung anhand fester Schwellenwerte.
    Gibt DataFrame mit Anomaliespalte zurück.
    """
    df["anomaly"] = df.apply(
        lambda row: -1 if (row["temperature"] > TEMP_THRESHOLD or row["vibration"] > VIB_THRESHOLD) else 1,
        axis=1
    )
    return df
