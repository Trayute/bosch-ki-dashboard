import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import webbrowser
import threading
import os

# === Daten laden ===
df = pd.read_csv("machine_data_with_anomalies.csv")
df["time"] = pd.to_datetime(df["time"])
df["status"] = df["anomaly"].map({1: "Normal", -1: "Anomalie"})

# Aufteilen in Normal- und Anomalie-Daten
df_normal = df[df["anomaly"] == 1]
df_anomal = df[df["anomaly"] == -1]

# === Dash App initialisieren ===
app = dash.Dash(__name__)
app.title = "Bosch KI Dashboard"

# === Temperatur-Plot ===
temperature_fig = go.Figure()

temperature_fig.add_trace(go.Scatter(
    x=df_normal["time"], y=df_normal["temperature"],
    mode="lines", name="Normal", line=dict(color="blue")
))
temperature_fig.add_trace(go.Scatter(
    x=df_anomal["time"], y=df_anomal["temperature"],
    mode="markers", name="Anomalie", marker=dict(color="red", size=8)
))
temperature_fig.update_layout(
    title="🌡️ Temperaturverlauf mit Anomalie-Erkennung",
    xaxis_title="Zeit",
    yaxis_title="Temperatur (°C)",
    legend_title="Status",
    template="plotly_white"
)

# === Vibrations-Plot ===
vibration_fig = go.Figure()

vibration_fig.add_trace(go.Scatter(
    x=df_normal["time"], y=df_normal["vibration"],
    mode="lines", name="Normal", line=dict(color="blue")
))
vibration_fig.add_trace(go.Scatter(
    x=df_anomal["time"], y=df_anomal["vibration"],
    mode="markers", name="Anomalie", marker=dict(color="red", size=8)
))
vibration_fig.update_layout(
    title="📈 Vibrationserkennung mit Anomalie-Markierung",
    xaxis_title="Zeit",
    yaxis_title="Vibration",
    legend_title="Status",
    template="plotly_white"
)

# === Layout definieren ===
app.layout = html.Div([
    html.H1("🔧 Bosch Maschinen-Dashboard mit KI", style={"textAlign": "center", "marginBottom": "40px"}),

    dcc.Graph(id="temperature-chart", figure=temperature_fig),
    dcc.Graph(id="vibration-chart", figure=vibration_fig),

    html.Div("🔵 = Normal | 🔴 = Anomalie", style={
        "textAlign": "center",
        "marginTop": "20px",
        "fontWeight": "bold",
        "fontSize": "18px"
    })
])

# === Autostart im Browser ===
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    print("🚀 Starte Dash-Server unter http://127.0.0.1:8050/")
    app.run(debug=True, use_reloader=False)
