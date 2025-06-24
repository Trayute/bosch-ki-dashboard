import pandas as pd
import numpy as np
import datetime

# Beispielhafte Maschinendaten erzeugen
np.random.seed(42)
data = {
    "time": [datetime.datetime.now() + datetime.timedelta(seconds=i*10) for i in range(10)],
    "temperature": np.random.normal(70, 5, 10),
    "vibration": np.random.normal(0.02, 0.005, 10)
}

df = pd.DataFrame(data)

# Speichern der Daten
df.to_csv("machine_data.csv", index=False)
print("✅ Datei machine_data.csv wurde erzeugt.")

import os

if os.path.exists("machine_data.csv"):
    print("✅ Datei erfolgreich erstellt.")
else:
    print("❌ Datei wurde NICHT erstellt!")
