import plotly.graph_objects as go
from app.agp import compute_agp

def plot_time_series(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["glucose"],
        mode="lines+markers",
        name="Glucose (mg/dL)"
    ))
    fig.update_layout(
        title="CGM Time Series",
        xaxis_title="Timestamp",
        yaxis_title="Glucose (mg/dL)",
        yaxis=dict(range=[40, 400]),
        template="plotly_white"
    )
    return fig

def plot_agp(df):
    agp = compute_agp(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=agp["time"], y=agp["p90"],
        line=dict(width=0), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=agp["time"], y=agp["p10"],
        fill='tonexty', fillcolor='rgba(173,216,230,0.2)',
        name='10–90%'
    ))
    fig.add_trace(go.Scatter(
        x=agp["time"], y=agp["q3"],
        line=dict(width=0), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=agp["time"], y=agp["q1"],
        fill='tonexty', fillcolor='rgba(30,144,255,0.3)',
        name='IQR (25–75%)'
    ))
    fig.add_trace(go.Scatter(
        x=agp["time"], y=agp["median"],
        mode='lines', name='Median',
        line=dict(color='blue', width=2)
    ))
    fig.update_layout(
        title="AGP Profile",
        xaxis_title="Time of Day",
        yaxis_title="Glucose (mg/dL)",
        yaxis=dict(range=[40, 400]),
        template="plotly_white"
    )
    return fig
