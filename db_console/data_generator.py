#DB-Analyzer Data Generator
import numpy as np
import datetime
import csv

col_names = ['from_station', 'to_station',  'departure', 'arrival', 'stops', 'price', 'ticket_type', 'train_type']
stations = ['Munich','Berlin','Hamburg','Frankfurt','Köln','Dresden']
ticket_type = ['Flexipreis', 'Sparpreis', 'FrankLu', "chidamba"]
train_type = ['ICE','RB','SBAHN']
base_date = datetime.datetime.now()
dates = date_list = [base_date + datetime.timedelta(hours=x) for x in range(0, 24)]

data=[]
with open('dummy_data.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(col_names)
    for x in range(0,100):
        row=[]
        f_st=''
        t_st=''
        while f_st is t_st:
            f_st = stations[np.random.randint(0,5)]
            t_st = stations[np.random.randint(0,5)]
        #Add from and to stations
        row +=[f_st,t_st]
        times = np.random.randint(0,7,2)
        #Add departure and arrival times
        row +=[base_date+datetime.timedelta(hours=float(times[0])),base_date+datetime.timedelta(hours=float(times[0]+times[1]))]
        #Add # stops
        row += [np.random.randint(0,3)]
        #Add price
        row += [np.random.randint(19,265)]
        #Add Ticket Tyoep
        row += [ticket_type[np.random.randint(4)]]
        #Add Train Type
        row += [train_type[np.random.randint(3)]]
        writer.writerow(row)

print('done.')


