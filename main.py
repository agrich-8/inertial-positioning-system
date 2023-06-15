import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import pandas as pd

pd.options.plotting.backend = "plotly"
# pd.options.display.max_columns = 100

df = pd.read_csv("data.txt", sep="\t")    #read text data into pandas DataFrame

df['vel'] = ''
print(df)

def vel(t1,t2,a):
    dateFormatter = "%H:%M:%S.%f"
    t1 = datetime.strptime(t1, dateFormatter)
    t2 = datetime.strptime(t2, dateFormatter)
    delta = t2-t1
    diff_velocity = delta.microseconds / 100000 * a
    
    return diff_velocity
    
diff_velocity = list(map(vel, df['Time'], df['Time'][1:], df['AccY(g)']))
inst_velocity = 0

for i in range(0, len(df['vel'].index)-1):
    inst_velocity += diff_velocity[i]
    df.at[i, 'vel'] = inst_velocity
    
print(df)
df = df['vel']
fig = df.plot(title="Pandas Backend Example", template="simple_white",
              labels=dict(index="time", value="money", variable="option"))
fig.update_yaxes(tickprefix="$")
fig.show()