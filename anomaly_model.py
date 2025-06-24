import pandas as pd

# 1. Beispielhafte Daten erzeugen und speichern
data = {
    "temperature": [72, 85, 79, 90, 65],
    "vibration": [0.03, 0.05, 0.02, 0.06, 0.01]
}

df = pd.DataFrame(data)
df.to_csv("machine_data.csv", index=False)
print("✅ machine_data.csv wurde erzeugt.")

# 2. Datei einlesen
df = pd.read_csv("machine_data.csv")
print("📊 Eingelesene Daten:")
print(df)

# 3. Anomalieerkennung durchführen
df["anomaly"] = (
    (df["temperature"] > 80) |
    (df["vibration"] > 0.04)
)

# 4. Ergebnis speichern
df.to_csv("machine_data_with_anomalies.csv", index=False)
print("✅ Datei machine_data_with_anomalies.csv wurde erzeugt.")
