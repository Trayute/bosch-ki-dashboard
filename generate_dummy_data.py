import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# === Parameter ===
NUM_POINTS = 1000  # Anzahl der Datenpunkte (je mehr, desto aussagekräftiger)
ANOMALY_RATE = 0.1  # 10% der Daten sollen Anomalien enthalten
TIME_INTERVAL = 10  # Zeitabstand zwischen den Messpunkten in Sekunden
OUTPUT_FOLDER = "data"
FILENAME = f"machine_data_with_anomalies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# === Listen vorbereiten ===
times = []
temperatures = []
vibrations = []
anomalies = []

# === Startzeit festlegen ===
start_time = datetime.now()

# === Datenpunkte generieren ===
for i in range(NUM_POINTS):
    # Zeitstempel erzeugen
    current_time = start_time + timedelta(seconds=i * TIME_INTERVAL)
    times.append(current_time)

    # Normale Messwerte
    temp = np.random.normal(loc=72, scale=3)      # Temperatur in °C
    vib = np.random.normal(loc=0.018, scale=0.003)  # Vibration

    # Mit einer Wahrscheinlichkeit von ANOMALY_RATE Anomalie erzeugen
    if np.random.rand() < ANOMALY_RATE:
        temp += np.random.choice([-1, 1]) * np.random.uniform(10, 20)
        vib += np.random.choice([-1, 1]) * np.random.uniform(0.01, 0.02)
        anomalies.append(-1)
    else:
        anomalies.append(1)

    temperatures.append(temp)
    vibrations.append(abs(vib))  # Vibrationswerte immer positiv

# === DataFrame erzeugen ===
df = pd.DataFrame({
    "time": times,
    "temperature": temperatures,
    "vibration": vibrations,
    "anomaly": anomalies
})

# === Ordner erstellen (falls nicht vorhanden) ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === Daten speichern ===
output_path = os.path.join(OUTPUT_FOLDER, FILENAME)
df.to_csv(output_path, index=False)

# === Erfolgsmeldung ===
print(f"✅ Datei erfolgreich gespeichert unter: {output_path}")
