import pandas as pd
import os

def detect_anomalies(infile=os.path.join("data", "machine_data.csv"),
                     outfile=os.path.join("data", "machine_data_with_anomalies.csv")):
    """
    Erkenne Anomalien basierend auf Schwellenwerten.
    """

    if not os.path.exists(infile):
        print(f"❌ Eingabedatei nicht gefunden: {infile}")
        return

    df = pd.read_csv(infile)
    df["time"] = pd.to_datetime(df["time"], errors='coerce')

    # Anomalie-Logik (kann angepasst werden)
    df["anomaly"] = 1
    df.loc[
        (df["temperature"] > 85) | (df["vibration"] > 0.04),
        "anomaly"
    ] = -1

    df.to_csv(outfile, index=False)
    print(f"✅ Anomalien erkannt und gespeichert unter: {outfile}")

if __name__ == "__main__":
    detect_anomalies()
