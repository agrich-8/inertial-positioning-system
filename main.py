import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import pandas as pd

pd.options.plotting.backend = "plotly"
# pd.options.display.max_columns = 100

df = pd.read_csv("data/straight-line-x-axis200Hz.txt", sep="\t")    #read text data into pandas DataFrame

df['vel'] = ''
print(df)

# def error_search(prev_acc, acc, subs_acc):
#     avg_acc = abs(prev_acc + subs_acc) * 3 
#     if abs(acc) > avg_acc and abs(acc) - avg_acc > 0.3:
#         print(acc, prev_acc, subs_acc)


# diff_distance = list(map(error_search, 
#                          df['AccX(g)'], 
#                          df['AccX(g)'][1:], 
#                          df['AccX(g)'][2:]
#                          )
#                     )

def vel(t1,t2,a):
    dateFormatter = "%H:%M:%S.%f"
    t1 = datetime.strptime(t1, dateFormatter)
    t2 = datetime.strptime(t2, dateFormatter)
    delta = t2-t1
    # diff_velocity = delta.microseconds / 100000 * a
    diff_velocity = 0.01 * (a) * 9.8
    return diff_velocity
    
diff_velocity = list(map(vel, df['Time'], df['Time'][1:], df['AccX(g)']))
inst_velocity = 0

for i in range(0, len(df['vel'].index)-1):
    inst_velocity += diff_velocity[i]
    df.at[i, 'vel'] = inst_velocity


df['dis'] = ''

def distance(t1,t2,v):
    dateFormatter = "%H:%M:%S.%f"
    t1 = datetime.strptime(t1, dateFormatter)
    t2 = datetime.strptime(t2, dateFormatter)
    delta = t2-t1
    # diff_distance = delta.microseconds / 100000 * v
    diff_distance = 0.01 * v
    print(v)
    return diff_distance
    
diff_distance = list(map(distance, df['Time'], df['Time'][1:], df['vel']))
inst_distance = 0

for i in range(0, len(df['dis'].index)-1):
    inst_distance += diff_distance[i]
    df.at[i, 'dis'] = inst_distance

print(list(df['vel']))
print(diff_distance[:5])
print(diff_velocity)
print(df)
# df = df['dis']
# fig = df.plot(title="Acceleration data", template="simple_white",
#               labels=dict(index="time", value="dis", variable="option"))
# fig.show()

fig = go.Figure()
fig = make_subplots(rows=1, cols=2, subplot_titles=('Plot 1', 'Plot 2'))

fig.add_trace(go.Scatter(x=df['AccY(g)'], y=df['AccX(g)'], mode='markers', name='Acceleration X',
                         marker=dict(color=list(range(0, df.shape[0])), colorbar=dict(title="h(x)=sin(x)"))), row=1, col=1)
fig.add_trace(go.Scatter(x=df['AccY(g)'], y=df['AccX(g)'], mode='markers', name='Acceleration Y',
                         marker=dict(color='#00CC96', size=5, line=dict(color='MediumPurple', width=1))
                         ), 
              row=1, 
              col=2
              )
fig.update_layout(legend_orientation='h',
                #   margin=dict(l=0, r=0, t=40, b=0),
                  legend=dict(x=.5, xanchor='center'),
                #   hovermode='x'
                  )
fig.update_layout(title='Plot Title')

fig.update_xaxes(title='Ось X графика 1', col=1, row=1)
fig.update_xaxes(title='Ось X графика 2', col=2, row=1)
fig.update_yaxes(title='Ось Y графика 1', col=1, row=1)
fig.update_yaxes(title='Ось Y графика 2', col=2, row=1)

fig.update_traces(hoverinfo='all', hovertemplate='Аргумент: %{x}<br>Функция: %{y}')

fig.show()
