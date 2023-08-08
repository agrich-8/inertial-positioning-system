import plotly.graph_objects as go
import pandas as pd

pd.options.plotting.backend = "plotly"


def show_3d_fig(
        df,
        x, 
        y, 
        z,
        title = None,
        name = None, 
        line=dict(color='MediumPurple', width=1),
        color=None,
        colorbar = dict(title="Time")):
    
    if color is None:
        color=list(range(0, df.shape[0]))
    
    fig = go.Figure()
    
    fig.add_trace(
            go.Scatter3d(
                name=name,
                x=df[x], 
                y=df[y], 
                z=df[z], 
                mode='markers', 
                marker=dict(size=3, color=color, line=line, colorbar=colorbar)))
    
    fig.update_layout(
            title=title,
            legend_orientation='h',
            #   margin=dict(l=0, r=0, t=40, b=0),
            legend=dict(x=.5, xanchor='center'),
            scene=go.layout.Scene(
                    xaxis=go.layout.scene.XAxis(title=x),
                    yaxis=go.layout.scene.YAxis(title=y),
                    zaxis=go.layout.scene.ZAxis(title=z),
                    # set default "camera" view
                    # camera=dict(eye=dict(x=1.4, y=1.5, z=0.3))
                    ))
    
    return fig


df_mag_test = pd.read_csv("data/mag_test.txt", sep="\t")

fig_acc = show_3d_fig(
    df=df_mag_test,
    title='Magnetometer test',
    x='MagX(μt)',
    y='MagY(μt)',
    z='MagZ(μt)',
    )
fig_acc.show()