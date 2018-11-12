# bahn-price-analyzer
Analyzing the prices of the Deutsche Bahn (based on project [juliuste/db-prices](https://github.com/juliuste/db-prices))

Small terminal application for the given API.

# Getting started
clone the directory and run 
1. `npm install`
2. setup aliases to run command from everywhere (WIP)

# Example commands
At the moment you can only specify the place by giving the exact station name, which can be found inside `stations.csv`. (still in progress, maybe we'll fix it with fuzzy matching)

`python db_console/db_info.py -f "Oldenburg (Oldb) Hbf" -t "München Hbf" -fd 2018-12-15 -td 2018-12-24`

![demo screenshot](demo/screenshot01.png)

## User program wrapper:

`python db_console/db_user_program.py`
![demo screenshot](demo/screenshot02.png)

# Node script
execute with `node scrapper.js -f from_station -t to_station -s start_date -e end_date`
 will write data into file: 

`data.csv`


# CSV file: data.csv
column names: date, hour, departure_time, arrival_time, stops, price, ticket_type, train_type

departure and arrival format:
'2017-06-05T08:53:00.000Z'

