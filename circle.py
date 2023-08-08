import plotly.graph_objects as go
import pandas as pd


df_pipe_1 = pd.read_csv("data/circle_1_sector.txt", sep="\t")
df_pipe_4 = pd.read_csv("data/circle_2_sector.txt", sep="\t")
df_pipe_2 = pd.read_csv("data/circle_3_sector.txt", sep="\t")
df_pipe_3 = pd.read_csv("data/circle_4_sector.txt", sep="\t")



fig = go.Figure()

fig.add_trace(
        go.Scatter3d(
            name='sector 1',
            x=df_pipe_1['AngleX(°)'], 
            y=df_pipe_1['AngleY(°)'], 
            z=df_pipe_1['AngleZ(°)'], 
            mode='markers', 
            marker=dict(size=3, color='#03fca5', line=dict(color='MediumPurple', width=0))))

fig.add_trace(
        go.Scatter3d(
            name='sector 2',
            x=df_pipe_2['AngleX(°)'], 
            y=df_pipe_2['AngleY(°)'], 
            z=df_pipe_2['AngleZ(°)'], 
            mode='markers', 
            marker=dict(size=3, color='#fca503', line=dict(color='MediumPurple', width=0))))

fig.add_trace(
        go.Scatter3d(
            name='sector 3',
            x=df_pipe_3['AngleX(°)'], 
            y=df_pipe_3['AngleY(°)'], 
            z=df_pipe_3['AngleZ(°)'], 
            mode='markers', 
            marker=dict(size=3, color='#3443eb', line=dict(color='MediumPurple', width=0))))

fig.add_trace(
        go.Scatter3d(
            name='sector 4',
            x=df_pipe_4['AngleX(°)'], 
            y=df_pipe_4['AngleY(°)'], 
            z=df_pipe_4['AngleZ(°)'], 
            mode='markers', 
            marker=dict(size=3, color='#fc0377', line=dict(color='MediumPurple', width=0))))

fig.update_layout(
        title='Сomparison of 1, 2, 3, 4 sectors acceleration graphs',
        width=1000, 
        height=800,
        legend_orientation='h',
        legend=dict(x=.5, xanchor='center'),
        scene=go.layout.Scene(
                xaxis=go.layout.scene.XAxis(title='AngleX(°)'),
                yaxis=go.layout.scene.YAxis(title='AngleY(°)'),
                zaxis=go.layout.scene.ZAxis(title='AngleZ(°)')
                ))
    
fig.show()



df_pipe_1 = pd.read_csv("data/circle_1_sector.txt", sep="\t")
df_pipe_4 = pd.read_csv("data/circle_2_sector.txt", sep="\t")
df_pipe_2 = pd.read_csv("data/circle_3_sector.txt", sep="\t")
df_pipe_3 = pd.read_csv("data/circle_4_sector.txt", sep="\t")


fig = go.Figure()

fig.add_trace(
        go.Scatter3d(
            name='sector 1',
            x=df_pipe_1['AccX(g)'], 
            y=df_pipe_1['AccY(g)'], 
            z=df_pipe_1['AccZ(g)'], 
            mode='markers', 
            marker=dict(size=3, color='#03fca5', line=dict(color='MediumPurple', width=1))))

fig.add_trace(
        go.Scatter3d(
            name='sector 2',
            x=df_pipe_2['AccX(g)'], 
            y=df_pipe_2['AccY(g)'], 
            z=df_pipe_2['AccZ(g)'], 
            mode='markers', 
            marker=dict(size=3, color='#fca503', line=dict(color='MediumPurple', width=1))))

fig.add_trace(
        go.Scatter3d(
            name='sector 3',
            x=df_pipe_3['AccX(g)'], 
            y=df_pipe_3['AccY(g)'], 
            z=df_pipe_3['AccZ(g)'], 
            mode='markers', 
            marker=dict(size=3, color='#3443eb', line=dict(color='MediumPurple', width=1))))

fig.add_trace(
        go.Scatter3d(
            name='sector 4',
            x=df_pipe_4['AccX(g)'], 
            y=df_pipe_4['AccY(g)'], 
            z=df_pipe_4['AccZ(g)'], 
            mode='markers', 
            marker=dict(size=3, color='#fc0377', line=dict(color='MediumPurple', width=1))))

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
