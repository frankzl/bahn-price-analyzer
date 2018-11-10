import pandas as pd
from termgraph_api.termgraph import *
import webbrowser
import datetime
import sys
from pprint import pprint

def custom_min(data):
    print("-----")
    idx = data["price"].idxmin()
    print(data.loc[idx])
    return data.loc[idx]

def analyze(filename):
    df = pd.read_csv(filename)
    base_url = 'https://link.bahn.guru/?journey='
    url_end = '&bc=0&class=2'


    df['departure_time'] = pd.to_datetime(df['departure_time'])
    # grouped = df.groupby(df['date']).min()
    grouped = df.groupby( df['date']).apply(custom_min)
    print(grouped)

    url_list = list(grouped['fulltxt'])
    pprint(grouped['fulltxt'])
    print('Ticket Prices:\n')
    dep_time_t = list(grouped['departure_time'])
    dep_time = []
    for i in range(len(dep_time_t)):
        dep_time += [str(i+1)+'. '+str(dep_time_t[i])]

    draw_graph(dep_time, list(grouped['price']))

    print('\n')

    print('Type index number to book or -1 to exit: ')
    ind = int(input())
    if ind is -1:
        sys.exit()
    else:
        try:
            redir = url_list[ind]
            url = base_url+redir+url_end
            print('opening db.de in new tab...')
            print(url_list)
            webbrowser.open_new_tab(url)
        except Exception as e:
            print('Invalid index entered. Exiting.')
            sys.exit()
    #plt.show()s
    return True
