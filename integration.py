from datetime import datetime
import pandas as pd
from functools import reduce

pd.options.plotting.backend = "plotly"
# pd.options.display.max_columns = 100

df = pd.read_csv("data/dormant_state_20Hz.txt", sep="\t")
df['vel'] = ''


def vel(t1,t2,a):
    dateFormatter = "%H:%M:%S.%f"
    t1 = datetime.strptime(t1, dateFormatter)
    t2 = datetime.strptime(t2, dateFormatter)
    delta = t2-t1
    diff_velocity = 0.01 * (a) * 9.8 + 0.0009
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

lst_avg = reduce(lambda x, y: x + y, diff_distance) / len(diff_distance)
print(lst_avg)
df = df['dis']
fig = df.plot(title="Acceleration data", template="simple_white",
              labels=dict(index="время", value="расстояние (м)", variable="option"))
fig.show()