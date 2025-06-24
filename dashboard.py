import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import webbrowser
import threading

# CSV laden
df = pd.read_csv("machine_data_with_anomalies.csv")
df["time"] = pd.to_datetime(df["time"])
df["status"] = df["anomaly"].map({1: "Normal", -1: "Anomalie"})

# Zwei DataFrames: normal & anomal
df_normal = df[df["anomaly"] == 1]
df_anomal = df[df["anomaly"] == -1]

# Dash-App erstellen
app = dash.Dash(__name__)
app.title = "Bosch KI Dashboard"

app.layout = html.Div([
    html.H1("Bosch Maschinen-Dashboard mit KI", style={"textAlign": "center"}),

    # Temperatur-Plot
    dcc.Graph(
        id="temperature-chart",
        figure={
            "data": [
                # Normale Daten als Linie
                px.line(df_normal, x="time", y="temperature").data[0],
                # Anomalien als Marker
                px.scatter(df_anomal, x="time", y="temperature",
                           color_discrete_sequence=["red"], labels={"status": "Anomalie"}).data[0]
            ],
            "layout": {
                "title": "Temperaturverlauf mit Anomalie-Erkennung",
                "xaxis": {"title": "Zeit"},
                "yaxis": {"title": "Temperatur (°C)"},
                "legend": {"title": "Status"},
            }
        }
    ),

    # Vibrations-Plot
    dcc.Graph(
        id="vibration-chart",
        figure={
            "data": [
                px.line(df_normal, x="time", y="vibration").data[0],
                px.scatter(df_anomal, x="time", y="vibration",
                           color_discrete_sequence=["red"]).data[0]
            ],
            "layout": {
                "title": "Vibrationserkennung",
                "xaxis": {"title": "Zeit"},
                "yaxis": {"title": "Vibration"},
                "legend": {"title": "Status"},
            }
        }
    ),

    html.Div("Grün = normal, Rot = Anomalie (Kreis)", style={"textAlign": "center", "marginTop": "20px"})
])

# Browser automatisch öffnen
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# App starten
if __name__ == "__main__":
    print("🚀 Starte Dash-Server...")
    import webbrowser
import os

if __name__ == '__main__':
    # Nur im Hauptprozess öffnen, nicht im Debug-Neustart
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open_new("http://127.0.0.1:8050/")
    app.run(debug=True)

