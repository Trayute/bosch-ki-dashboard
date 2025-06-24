import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import webbrowser
import threading

# Daten laden
df = pd.read_csv("machine_data_with_anomalies.csv")
df["time"] = pd.to_datetime(df["time"])
df["status"] = df["anomaly"].map({1: "Normal", -1: "Anomalie"})

# Dash App definieren
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Bosch Maschinen-Dashboard mit KI", style={"textAlign": "center"}),

    dcc.Graph(
        id="temperature-chart",
        figure=px.line(df, x="time", y="temperature", color="status",
                       title="Temperaturverlauf mit Anomalie-Erkennung")
    ),

    dcc.Graph(
        id="vibration-chart",
        figure=px.line(df, x="time", y="vibration", color="status",
                       title="Vibrationserkennung")
    ),

    html.Div("Grün = normal, Rot = Anomalie", style={"textAlign": "center", "marginTop": "20px"})
])

# Funktion zum automatischen Öffnen des Browsers
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Starte den Dash-Server
if __name__ == "__main__":
    print("🚀 Starte Dash-Server...")
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)

