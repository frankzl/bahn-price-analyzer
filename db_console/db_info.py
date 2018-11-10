#Wrapper for our analyzer
#get_user_request
#send_request
#analyze(filename)

import argparse
import numpy as numpy
import pprint

def send_request(args):
    args_req =     args = '-f '+' '.join(args.from_d) + ' -t '+' '.join(args.to) + ' -s '+args.from_date + ' -e '+args.to_date
    request = 'node ../scrapper.js '+args_req
    print(request)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_d', '-f', help='From station', nargs='+', required = True)
    parser.add_argument('--to', '-t', help='To station', nargs='+', required=True)
    parser.add_argument('--from-date', '-fd', help='Start of date range(yyyy-mm-dd)', required=True)
    parser.add_argument('--to-date', '-td', help='End of Date range(yyyy-mm-dd)', required=True)

    args = parser.parse_args()
    
    response = send_request(args)


    print(args)
