import subprocess

print("🎛 1. Erzeuge Maschinendaten...")
subprocess.run(["python", "simulate_data.py"])

print("🧠 2. Erkenne Anomalien...")
subprocess.run(["python", "analyze_data.py"])

print("🖥 3. Starte Dashboard im Browser...")
subprocess.Popen(["python", "dashboard.py"])  # ← wichtig: Popen statt run
