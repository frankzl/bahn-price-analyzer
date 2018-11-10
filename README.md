# bahn-price-analyzer
Analyzing the prices of the Deutsche Bahn (based on juliuste's project)

# Getting started
clone the directory and run `npm install`

# Node script
execute with `node scrapper.js -f from_station -t to_station -s start_date -e end_date`
 will write data into file: 

`data.csv`


# CSV file: data.csv
column names: date, hour, departure_time, arrival_time, stops, price, ticket_type, train_type

departure and arrival format:
'2017-06-05T08:53:00.000Z'

