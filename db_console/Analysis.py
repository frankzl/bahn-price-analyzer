import pandas as pd
from termgraph_api.termgraph import *

import matplotlib.pyplot as plt
import datetime


def analyze(filename):
    df = pd.read_csv(filename)

    #print(df.head(2))

    df['departure_time'] = pd.to_datetime(df['departure_time'])

    #df[0] = str(datetime.date(int(df[0]), int(df[1]), int(df[2])))
    #print(df.head(2))

    grouped = df.groupby(df['date']).min()

    print('Ticket Prices:\n')

    draw_graph(list(grouped['departure_time']), list(grouped['price']))

    print('\n')
    #plt.show()s

    if __name__ is '__main__':
        print('here')
        analyze('data.csv')