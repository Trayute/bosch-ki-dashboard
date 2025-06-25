import pandas as pd
import os

# === Parameter ===
INPUT_FILE = "machine_data.csv"
OUTPUT_FILE = "machine_data_with_anomalies.csv"

# === Schwellenwerte für Anomalien ===
THRESHOLDS = {
    "temperature": 80,      # Temperaturgrenze in °C
    "vibration": 0.04       # Vibrationsgrenze
}

def detect_anomalies(file_in=INPUT_FILE, file_out=OUTPUT_FILE):
    if not os.path.exists(file_in):
        print(f"❌ Eingabedatei '{file_in}' nicht gefunden.")
        return

    df = pd.read_csv(file_in)
    df["time"] = pd.to_datetime(df["time"], errors='coerce')

    df["anomaly"] = (
        (df["temperature"] > THRESHOLDS["temperature"]) |
        (df["vibration"] > THRESHOLDS["vibration"])
    ).map({True: -1, False: 1})

    df.to_csv(file_out, index=False)
    print(f"✅ Anomalien erkannt und gespeichert unter: {file_out}")
    return df

if __name__ == "__main__":
    detect_anomalies()
