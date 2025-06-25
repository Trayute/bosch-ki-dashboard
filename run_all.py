import os
import subprocess
import shutil

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_file_preview(path, lines=5):
    print(f"\n📄 Vorschau von: {path}")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for i in range(lines):
                line = f.readline()
                if not line:
                    break
                print("   ", line.strip())
    else:
        print("   ❌ Datei nicht gefunden.")

def step(title, command, output_file=None):
    print(f"\n🔄 {title}")
    print(f"▶ Befehl: {command}")
    result = subprocess.run(["python", command], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("❌ Fehler:", result.stderr)
    if output_file:
        log_file_preview(output_file)

if __name__ == "__main__":
    clear_console()
    print("🚀 Starte Bosch KI-Maschinendashboard\n")

    step("1/3: Simuliere neue Maschinendaten", "simulate_data.py", "data/machine_data.csv")

    step("2/3: Erkenne Anomalien", "analyze_data.py", "data/machine_data_with_anomalies.csv")

    print("\n🖥 3/3: Starte Dashboard unter http://127.0.0.1:8050/")
    print("🌐 Wenn kein Tab geöffnet wird, öffne bitte manuell deinen Browser.\n")

    subprocess.run(["python", "dashboard.py"])
