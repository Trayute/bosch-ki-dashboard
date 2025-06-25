import pandas as pd

THRESHOLDS = {
    "temperature": 80,
    "vibration": 0.04
}

def detect_anomalies(file_in="machine_data.csv", file_out="machine_data_with_anomalies.csv"):
    df = pd.read_csv(file_in)
    df["time"] = pd.to_datetime(df["time"])

    df["anomaly"] = (
        (df["temperature"] > THRESHOLDS["temperature"]) |
        (df["vibration"] > THRESHOLDS["vibration"])
    )
    df["anomaly"] = df["anomaly"].map({True: -1, False: 1})

    df.to_csv(file_out, index=False)
    print(f"✅ '{file_out}' mit Anomalien gespeichert.")
    return df

if __name__ == "__main__":
    detect_anomalies()
