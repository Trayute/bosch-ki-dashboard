import dash
from dash import dcc, html
import plotly.express as px  # ← WICHTIG
import pandas as pd
import webbrowser
import threading
import os


# Daten laden
df = pd.read_csv("machine_data_with_anomalies.csv")
df["time"] = pd.to_datetime(df["time"])
df["status"] = df["anomaly"].map({1: "Normal", -1: "Anomalie"})

# Aufteilen in Normal- und Anomalie-Daten
df_normal = df[df["anomaly"] == 1]
df_anomal = df[df["anomaly"] == -1]

# Dash App initialisieren
app = dash.Dash(__name__)
app.title = "Bosch KI Dashboard"

# Layout der App
app.layout = html.Div([
    html.H1("Bosch Maschinen-Dashboard mit KI", style={"textAlign": "center"}),

    # Temperatur-Plot
    dcc.Graph(
        id="temperature-chart",
        figure={
            "data": [
                # Normale Linie
                px.line(df_normal, x="time", y="temperature").data[0],
                # Anomalien explizit als rote Marker
                dict(
                    type="scatter",
                    mode="markers",
                    x=df_anomal["time"],
                    y=df_anomal["temperature"],
                    marker=dict(color="red", size=10),
                    name="Anomalie"
                )
            ],
            "layout": {
                "title": "Temperaturverlauf mit Anomalie-Erkennung",
                "xaxis": {"title": "Zeit", "autorange": True},
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
                dict(
                    type="scatter",
                    mode="markers",
                    x=df_anomal["time"],
                    y=df_anomal["vibration"],
                    marker=dict(color="red", size=10),
                    name="Anomalie"
                )
            ],
            "layout": {
                "title": "Vibrationserkennung",
                "xaxis": {"title": "Zeit", "autorange": True},
                "yaxis": {"title": "Vibration"},
                "legend": {"title": "Status"},
            }
        }
    ),


    html.Div("🔵 = Normal | 🔴 = Anomalie", style={"textAlign": "center", "marginTop": "20px", "fontWeight": "bold"})
])

# Autostart im Browser
if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open_new("http://127.0.0.1:8050/")
    print("🚀 Starte Dash-Server...")
    app.run(debug=True)
