import numpy as np
import plotly.graph_objects as go


def standing_katz(
    z_function,
    tpr_values,
    ppr_min=0.2,
    ppr_max=15,
    points=150,
    custom_ppr=None,
    custom_tpr=None,
):
    ppr = np.linspace(ppr_min, ppr_max, points)

    fig = go.Figure()

    for tpr in tpr_values:

        z = [
            z_function(p, tpr)
            for p in ppr
        ]

        fig.add_trace(
            go.Scatter(
                x=ppr,
                y=z,
                mode="lines",
                name=f"Tpr = {tpr}",
            )
        )

    fig.update_layout(
        title="Chart",
        xaxis_title="Pseudo-reduced Pressure (Ppr)",
        yaxis_title="Gas Compressibility Factor (Z)",
        template="plotly_white",
        legend_title="Reduced Temperature",
        height = 600
    )
    if custom_ppr is not None and custom_tpr is not None:
        fig.add_trace(
            go.Scatter(
                x=[custom_ppr],
                y=[ z_function(custom_ppr, custom_tpr)],
                mode="markers",
                marker=dict(
                    size=12,
                    color="red",
                    symbol="circle",
                ),
                name="Current State",
            )
            )

    return fig