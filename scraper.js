const prices = require('db-prices')

const moment = require('moment-timezone')
const {inspect} = require('util')

const tz = 'Europe/Berlin'

/*
prices('8000105', '8011160', when)
    .then((routes) => {
            console.log(inspect(routes, {depth: null}))
    })
    .catch((err) => {
        console.error(err)
        process.exit(1)
    })
*/


const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const csvWriter = createCsvWriter({
    path: 'data.csv',
    header: [
    {id: 'date', title: 'date'},
    {id: 'departure_time', title: 'departure_time'},
    {id: 'arrival_time', title: 'arrival_time'}    ,
    {id: 'stops', title: 'stops'}                  ,
    {id: 'price', title: 'price'}                  ,
    {id: 'tickettype', title: 'tickettype'}        ,
    ]
});

const writeDict = ( records ) => {
    csvWriter.writeRecords(records)       // returns a promise
        .then(() => {
            console.log('...Done');
        });
}
const dateToInt = function(date){
    const day = date.getDate()
        const month = date.getMonth() + 1
        const year = date.getFullYear()

        return year * 10000 + month * 100 + day
}



const getData = function ( from_id, to_id, from_date, to_date, prev_routes){

    const end = to_date
        const day = from_date

        if(end.getTime() < day.getTime()){
            console.log(prev_routes)
            writeDict( prev_routes)
            return
        }

    const when = moment.tz(day.getTime(), tz).hour(0).minute(0).second(0).day(day.getDay()).toDate()
    console.log(when.getDate())
    console.log(when.getMonth())
    console.log(when.getFullYear())
    console.log("------------")

        prices(from_id, to_id, when)
        .then((routes) => {
            // console.log(inspect(routes, {depth: null}))

            routes = routes.map( (route) => {
                return {
                    date: dateToInt(from_date),
                    departure_time: route.legs[0].departure,
                    arrival_time: route.legs[route.legs.length - 1].arrival,
                    stops: route.legs.length,
                    price: route.price.amount,
                    tickettype: route.price.name,
                }
            })
            const tomorrow = from_date
                tomorrow.setDate(tomorrow.getDate() + 1);
            getData( from_id, to_id, tomorrow, to_date, prev_routes.concat(routes))
        })
    .catch((err) => {
        console.error(err)
            process.exit(1)
    })

}


getData(8098160, 8000105, new Date("2018-11-18"), new Date("2018-11-19"), [])


const argv = require('minimist')(process.argv.slice(2));
console.dir(argv);

getData(argv.f, argv.t, new Date(argv.s), new Date(argv.e), [])




/*
   const stations = require('db-stations')
   stations()
   .on('data', function(data){
   console.log("{ name: \"" + data.name + "\", id: "+data.id + "},")
   })
   .on('error', console.error)
   */
