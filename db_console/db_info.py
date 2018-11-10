#Wrapper for our analyzer
#get_user_request
#send_request
#analyze(filename)

import argparse
import numpy as numpy
import pprint
from Naked.toolshed.shell import execute_js, muterun_js
from analysis import *
import pandas as pd
import sys
import os

#comment
def get_station_id(station_name):
    path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(os.path.join(path, "../stations.csv"))
    stations = dict(zip(list(df.name.str.upper()),list(df.id)))
    try:
        st_id = stations[station_name.upper()]
        return str(st_id)
    except Exception as e:
        print('{0} Please enter a valid station!'.format(station_name))
        sys.exit()
def send_request(args):
    args_req =     args = '-f '+get_station_id(' '.join(args.from_d)) + ' -t '+get_station_id(' '.join(args.to)) + ' -s '+args.from_date + ' -e '+args.to_date
    script = (os.path.dirname(os.path.realpath(__file__)) + "/../scraper.js")
    request = script + ' '+args_req
    print(request)
    result = execute_js(request)
    #result = True
    if result:
        return '/tmp/db-price-analysis/data.csv'
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_d', '-f', help='From station', nargs='+', required = True)
    parser.add_argument('--to', '-t', help='To station', nargs='+', required=True)
    parser.add_argument('--from-date', '-fd', help='Start of date range(yyyy-mm-dd)', required=True)
    parser.add_argument('--to-date', '-td', help='End of Date range(yyyy-mm-dd)', required=True)

    args = parser.parse_args()
    
    response = send_request(args)

    if response is not None:
        #call analyzer()
        print('Trains between {0} ---> {1}\n'.format(' '.join(args.from_d), ' '.join(args.to)))
        result = analyze(response)
    else:
        print('Error fetching Data...')
    
#