import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# === Parameter ===
NUM_POINTS = 1000
ANOMALY_RATE = 0.1
TIME_INTERVAL = 10  # Sekunden
OUTPUT_FOLDER = "data"
FILENAME = "machine_data.csv"  # Fester Dateiname für konsistente Nutzung

# === Listen vorbereiten ===
times = []
temperatures = []
vibrations = []
anomalies = []

# === Startzeit festlegen ===
start_time = datetime.now()

# === Datenpunkte generieren ===
for i in range(NUM_POINTS):
    current_time = start_time + timedelta(seconds=i * TIME_INTERVAL)
    times.append(current_time)

    temp = np.random.normal(loc=72, scale=3)
    vib = np.random.normal(loc=0.018, scale=0.003)

    if np.random.rand() < ANOMALY_RATE:
        temp += np.random.choice([-1, 1]) * np.random.uniform(10, 20)
        vib += np.random.choice([-1, 1]) * np.random.uniform(0.01, 0.02)
        anomalies.append(-1)
    else:
        anomalies.append(1)

    temperatures.append(temp)
    vibrations.append(abs(vib))  # Positiv halten

# === DataFrame erzeugen ===
df = pd.DataFrame({
    "time": times,
    "temperature": temperatures,
    "vibration": vibrations,
    "anomaly": anomalies
})

# === Ordner erstellen & speichern ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
output_path = os.path.join(OUTPUT_FOLDER, FILENAME)
df.to_csv(output_path, index=False)

print(f"✅ Datei erfolgreich gespeichert unter: {output_path}")
