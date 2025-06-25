import subprocess
import webbrowser
import time
import os

def run(command, msg):
    print(f"\n🔄 {msg}")
    result = subprocess.run(["python", command])
    if result.returncode != 0:
        print(f"❌ Fehler bei {command}")
        exit(1)

if __name__ == "__main__":
    print("🚀 Starte Bosch KI-Maschinendashboard\n")

    # Optional: echten großen Datensatz simulieren?
    if os.path.exists("generate_dummy_data.py"):
        user_choice = input("❓ Großen Simulationsdatensatz generieren (y/n)? ").strip().lower()
        if user_choice == "y":
            run("generate_dummy_data.py", "0/4: Erzeuge Dummy-Daten")
            print("⚠️  Nutze dann die erzeugte Datei manuell im Dashboard.")
    
    # Schritt 1: Simuliere einfache CSV (kleiner Demo-Datensatz)
    run("simulate_data.py", "1/4: Simuliere Maschinendaten")

    # Schritt 2: Führe Anomalie-Erkennung durch
    run("analyze_data.py", "2/4: Erkenne Anomalien in Daten")

    # Schritt 3: Starte Dashboard
    print("\n🖥 3/4: Starte Dashboard unter http://127.0.0.1:8050/")
    subprocess.Popen(["python", "dashboard.py"])

    # Schritt 4: Öffne Browser automatisch
    time.sleep(2)
    try:
        webbrowser.open("http://127.0.0.1:8050/")
        print("🌐 Dashboard im Browser geöffnet")
    except:
        print("⚠️ Konnte Browser nicht automatisch öffnen.")
