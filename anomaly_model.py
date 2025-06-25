import pandas as pd
import os

# === Parameter ===
TEMP_THRESHOLD = 80     # Temperaturgrenze für Anomalie (in °C)
VIB_THRESHOLD = 0.04    # Vibrationsgrenze für Anomalie
INPUT_FILE = "machine_data.csv"
OUTPUT_FILE = "machine_data_with_anomalies.csv"

# === 1. Beispielhafte Daten erzeugen (nur wenn Datei nicht existiert) ===
if not os.path.exists(INPUT_FILE):
    data = {
        "temperature": [72, 85, 79, 90, 65],
        "vibration": [0.03, 0.05, 0.02, 0.06, 0.01]
    }
    df = pd.DataFrame(data)
    df.to_csv(INPUT_FILE, index=False)
    print(f"✅ Beispielhafte Datei '{INPUT_FILE}' wurde erzeugt.")

# === 2. Datei einlesen ===
df = pd.read_csv(INPUT_FILE)
print("\n📊 Eingelesene Daten:")
print(df)

# === 3. Anomalie-Erkennung (regelbasiert) ===
df["anomaly"] = df.apply(
    lambda row: -1 if (row["temperature"] > TEMP_THRESHOLD or row["vibration"] > VIB_THRESHOLD) else 1,
    axis=1
)

print("\n🚨 Markierte Anomalien:")
print(df[["temperature", "vibration", "anomaly"]])

# === 4. Ergebnis speichern ===
df.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Datei mit Anomalien gespeichert unter: {OUTPUT_FILE}")
