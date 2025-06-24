import pandas as pd

# Daten laden
df = pd.read_csv("machine_data.csv")

# Sicherheitsprüfung
if "time" not in df.columns:
    raise ValueError("❌ 'time' Spalte fehlt. Wurde simulate_data.py korrekt ausgeführt?")

# Zeitspalte konvertieren
df["time"] = pd.to_datetime(df["time"])

# Anomalie erkennen
df["anomaly"] = (
    (df["temperature"] > 80) |
    (df["vibration"] > 0.04)
)

df["anomaly"] = df["anomaly"].map({True: -1, False: 1})

# Datei speichern
df.to_csv("machine_data_with_anomalies.csv", index=False)
print("✅ Datei machine_data_with_anomalies.csv wurde erzeugt.")
