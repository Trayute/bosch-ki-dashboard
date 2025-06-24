import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import webbrowser
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
        figure=go.Figure([
            go.Scatter(
                x=df_normal["time"],
                y=df_normal["temperature"],
                mode="lines",
                name="Normal",
                line=dict(color="blue")
            ),
            go.Scatter(
                x=df_anomal["time"],
                y=df_anomal["temperature"],
                mode="markers",
                name="Anomalie",
                marker=dict(color="red", size=10, symbol="circle")
            )
        ]).update_layout(
            title="Temperaturverlauf mit Anomalie-Erkennung",
            xaxis_title="Zeit",
            yaxis_title="Temperatur (°C)",
            legend_title="Status"
        )
    ),

    # Vibrations-Plot
    dcc.Graph(
        id="vibration-chart",
        figure=go.Figure([
            go.Scatter(
                x=df_normal["time"],
                y=df_normal["vibration"],
                mode="lines",
                name="Normal",
                line=dict(color="blue")
            ),
            go.Scatter(
                x=df_anomal["time"],
                y=df_anomal["vibration"],
                mode="markers",
                name="Anomalie",
                marker=dict(color="red", size=10, symbol="circle")
            )
        ]).update_layout(
            title="Vibration mit Anomalie-Erkennung",
            xaxis_title="Zeit",
            yaxis_title="Vibration",
            legend_title="Status"
        )
    ),

    html.Div("🔵 = Normal | 🔴 = Anomalie", style={"textAlign": "center", "marginTop": "20px", "fontWeight": "bold"})
])

# Autostart im Browser
if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open_new("http://127.0.0.1:8050/")
    print("🚀 Starte Dash-Server...")
    app.run(debug=True)
