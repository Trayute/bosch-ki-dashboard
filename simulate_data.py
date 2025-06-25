import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(n=100, start_time=None):
    """Simuliert Maschinendaten mit Anomalien und speichert sie"""
    start_time = start_time or datetime.now()
    timestamps = [start_time + timedelta(seconds=i * 10) for i in range(n)]

    temp = np.random.normal(70, 3, n)
    vib = np.random.normal(0.02, 0.01, n)
    pressure = np.random.normal(100, 5, n)

    # Anomalien zufällig setzen
    anomalies = [1] * n
    anomaly_indices = random.sample(range(n), k=int(n * 0.1))  # 10 % Anomalien
    for i in anomaly_indices:
        temp[i] += random.uniform(15, 25)
        vib[i] += random.uniform(0.02, 0.05)
        anomalies[i] = -1

    df = pd.DataFrame({
        "time": timestamps,
        "temperature": temp,
        "vibration": vib,
        "pressure": pressure,
        "anomaly": anomalies
    })

    # Speichere als "machine_data.csv", damit analyze_data.py sie weiterverarbeiten kann
    df.to_csv("machine_data.csv", index=False)
    print("✅ 'machine_data.csv' gespeichert.")

if __name__ == "__main__":
    generate_data()
