import plotly.graph_objects as go
import pandas as pd

pd.options.plotting.backend = "plotly"

df_r_side = pd.read_csv("data/r_side.txt", sep="\t")
df_l_side = pd.read_csv("data/l_side.txt", sep="\t")


fig = go.Figure()

fig.add_trace(
        go.Scatter3d(
            name='right side',
            x=df_r_side['AccX(g)'], 
            y=df_r_side['AccY(g)'], 
            z=df_r_side['AccZ(g)'], 
            mode='markers',
            marker=dict(size=3, color='#03fca5', line=dict(color='MediumPurple', width=1))))


fig.add_trace(
        go.Scatter3d(
            name='left side',
            x=df_l_side['AccX(g)'], 
            y=df_l_side['AccY(g)'], 
            z=df_l_side['AccZ(g)'], 
            mode='markers', 
            marker=dict(size=3, color='#3443eb', line=dict(color='MediumPurple', width=1))))


fig.update_layout(
        title='Сomparison of 1, 2, 3, 4 sectors acceleration graphs',
        width=1000, 
        height=800,
        legend_orientation='h',
        #   margin=dict(l=0, r=0, t=40, b=0),
        legend=dict(x=.5, xanchor='center'),
        scene=go.layout.Scene(
                xaxis=go.layout.scene.XAxis(title='AccX(g)'),
                yaxis=go.layout.scene.YAxis(title='AccY(g)'),
                zaxis=go.layout.scene.ZAxis(title='AccZ(g)'),
                # set default "camera" view
                # camera=dict(eye=dict(x=1.4, y=1.5, z=0.3))
                ))
    
fig.show()
