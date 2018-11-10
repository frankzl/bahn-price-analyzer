# bahn-price-analyzer
Analyzing the prices of the Deutsche Bahn (based on juliuste's project)

# Node script
execute with `node scrapper.js -f from_station -t to_station -d date`
 will write data into file: 

`from_station-to_station-date.csv`


# CSV file: data.csv
column names: from_station, to_station, departure, arrival, stops, price, ticket_type, train_type

departure and arrival format:
'2017-06-05T08:53:00.000Z'

