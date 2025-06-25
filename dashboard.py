import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html, Input, Output
import os
import webbrowser

DATA_FILE = os.path.join("data", "machine_data_with_anomalies.csv")

# Dash-App initialisieren
app = dash.Dash(__name__)
app.title = "Maschinen-Dashboard mit KI"

# Layout mit Intervall (alle 5 Sekunden)
app.layout = html.Div([
    html.H1("🔧 Maschinen-Dashboard mit KI", style={"textAlign": "center"}),

    dcc.Interval(id="interval-component", interval=5 * 1000, n_intervals=0),

    dcc.Graph(id="temperature-graph"),
    dcc.Graph(id="vibration-graph")
])

# Callback zur Aktualisierung
@app.callback(
    Output("temperature-graph", "figure"),
    Output("vibration-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_graphs(n):
    if not os.path.exists(DATA_FILE):
        return {}, {}

    df = pd.read_csv(DATA_FILE)
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # Temperatur-Plot
    temp_fig = {
        "data": [
            go.Scatter(
                x=df["time"],
                y=df["temperature"],
                mode="lines",
                name="Temperatur",
                line=dict(color="blue"),
            ),
            go.Scatter(
                x=df[df["anomaly"] == -1]["time"],
                y=df[df["anomaly"] == -1]["temperature"],
                mode="markers",
                name="Anomalie",
                marker=dict(color="red", size=8),
            ),
            go.Scatter(
                x=[df["time"].iloc[-1]],
                y=[df["temperature"].iloc[-1]],
                mode="markers+text",
                name="Letzter Wert",
                marker=dict(color="orange", size=10),
                text=["Letzter"],
                textposition="top center"
            )
        ],
        "layout": go.Layout(
            title="🌡️ Temperaturverlauf mit Anomalien",
            xaxis=dict(title="Zeit"),
            yaxis=dict(title="Temperatur (°C)"),
            template="plotly_white"
        )
    }

    # Vibrations-Plot
    vib_fig = {
        "data": [
            go.Scatter(
                x=df["time"],
                y=df["vibration"],
                mode="lines",
                name="Vibration",
                line=dict(color="green"),
            ),
            go.Scatter(
                x=df[df["anomaly"] == -1]["time"],
                y=df[df["anomaly"] == -1]["vibration"],
                mode="markers",
                name="Anomalie",
                marker=dict(color="red", size=8),
            ),
            go.Scatter(
                x=[df["time"].iloc[-1]],
                y=[df["vibration"].iloc[-1]],
                mode="markers+text",
                name="Letzter Wert",
                marker=dict(color="orange", size=10),
                text=["Letzter"],
                textposition="top center"
            )
        ],
        "layout": go.Layout(
            title="🪄 Vibration mit Anomalien",
            xaxis=dict(title="Zeit"),
            yaxis=dict(title="Vibration"),
            template="plotly_white"
        )
    }

    return temp_fig, vib_fig

# Browser automatisch öffnen
if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://127.0.0.1:8050/")
    app.run(debug=True, use_reloader=True)
