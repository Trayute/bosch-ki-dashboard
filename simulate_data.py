import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import time
import os

def generate_data(n=100,
                  step_seconds=10,
                  anomaly_ratio=0.10,
                  outfile=os.path.join("data", "machine_data.csv")):
    """
    Erstellt simulierte Maschinendaten mit Anomalien.
    """
    print("▶ simulate_data.py wird ausgeführt")


    os.makedirs("data", exist_ok=True)

    # Zufall mit Systemzeit initialisieren für Variation
    seed = int(time.time() * 1000) % 2**32  # Millisekunden-Genauigkeit
    np.random.seed(seed)
    random.seed(seed)

    start_time = datetime.now()
    timestamps = [start_time + timedelta(seconds=i * step_seconds) for i in range(n)]

    temp = np.random.normal(70, 3, n)
    vib  = np.random.normal(0.02, 0.01, n)
    pres = np.random.normal(100, 5, n)

    anomaly_flags = np.ones(n, dtype=int)
    k = int(n * anomaly_ratio)
    idx = random.sample(range(n), k=k)
    temp[idx] += np.random.uniform(15, 25, k)
    vib[idx]  += np.random.uniform(0.02, 0.05, k)
    anomaly_flags[idx] = -1

    df = pd.DataFrame({
        "time": timestamps,
        "temperature": temp,
        "vibration": vib,
        "pressure": pres,
        "anomaly": anomaly_flags
    })

    df.to_csv(outfile, index=False)
    print(f"✅ '{outfile}' geschrieben ({n} Zeilen).")

if __name__ == "__main__":
    generate_data(
        n=120,
        step_seconds=10,
        anomaly_ratio=0.10
    )
