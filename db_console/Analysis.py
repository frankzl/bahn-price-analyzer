import pandas as pd
from termgraph-api.termgraph.termgraph import *

import matplotlib.pyplot as plt
import datetime

df = pd.read_csv("data.csv")

#print(df.head(2))

df['departure_time'] = pd.to_datetime(df['departure_time'])

#df[0] = str(datetime.date(int(df[0]), int(df[1]), int(df[2])))
#print(df.head(2))

grouped = df.groupby(df['date']).min()

print(grouped)


#plt.plot(grouped['departure_time'], grouped['price'])
#plt.show()