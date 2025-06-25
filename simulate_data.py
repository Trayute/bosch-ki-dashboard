import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(n=100,
                  start_time=None,
                  step_seconds=10,
                  anomaly_ratio=0.10,
                  seed=None,
                  outfile="machine_data.csv"):
    """
    Erstellt eine simulierte Maschinen-Zeitreihe.

    Parameters
    ----------
    n : int                Anzahl der Messpunkte
    start_time : datetime  Start-Zeitpunkt (default = jetzt)
    step_seconds : int     Abstand zwischen Punkten
    anomaly_ratio : float  Anteil Anomalien (0-1)
    seed : int             Zufalls-Seed für Reproduzierbarkeit
    outfile : str          CSV-Dateiname
    """
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)

    start_time = start_time or datetime.now()
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
        start_time=datetime(2025, 6, 25, 12, 16, 0),
        step_seconds=10,
        anomaly_ratio=0.10,
        seed=42
    )
