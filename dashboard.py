import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html
import webbrowser
import os

# Korrigierter Pfad zur automatisch erzeugten Anomalie-Datei
DATA_PATH = "machine_data_with_anomalies.csv"

# Daten einlesen
df = pd.read_csv(DATA_PATH)

# Zeitspalte in Datetime konvertieren
df["time"] = pd.to_datetime(df["time"])

# Dash App initialisieren
app = dash.Dash(__name__)
app.title = "Bosch Maschinen-Dashboard mit KI"

# Layout definieren
app.layout = html.Div([
    html.H1("Bosch Maschinen-Dashboard mit KI", style={"textAlign": "center"}),

    dcc.Graph(
        id="temperature-graph",
        figure={
            "data": [
                go.Scatter(
                    x=df["time"],
                    y=df["temperature"],
                    mode="lines",
                    name="Normal",
                    line=dict(color="blue"),
                ),
                go.Scatter(
                    x=df[df["anomaly"] == 1]["time"],
                    y=df[df["anomaly"] == 1]["temperature"],
                    mode="markers",
                    name="Anomalie",
                    marker=dict(color="red", size=8),
                )
            ],
            "layout": go.Layout(
                title="🌡️ Temperaturverlauf mit Anomalie-Erkennung",
                xaxis={"title": "Zeit"},
                yaxis={"title": "Temperatur (°C)"},
                legend={"x": 0, "y": 1},
            )
        }
    ),

    dcc.Graph(
        id="vibration-graph",
        figure={
            "data": [
                go.Scatter(
                    x=df["time"],
                    y=df["vibration"],
                    mode="lines",
                    name="Normal",
                    line=dict(color="blue"),
                ),
                go.Scatter(
                    x=df[df["anomaly"] == 1]["time"],
                    y=df[df["anomaly"] == 1]["vibration"],
                    mode="markers",
                    name="Anomalie",
                    marker=dict(color="red", size=8),
                )
            ],
            "layout": go.Layout(
                title="🪄 Vibrations­erkennung mit Anomalie-Markierung",
                xaxis={"title": "Zeit"},
                yaxis={"title": "Vibration"},
                legend={"x": 0, "y": 1},
            )
        }
    )
])

# Browser nur im Hauptprozess öffnen
if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://127.0.0.1:8050/")
    app.run(debug=True, use_reloader=True)
