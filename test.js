const moment = require('moment-timezone')
const {inspect} = require('util')
const prices = require('db-prices')

const tz = 'Europe/Berlin'
// some monday in the future
const when = moment.tz(Date.now(), tz).hour(10).minute(30).second(0).day(1 + 7).toDate()

prices('8002549', '8098096', when)
.then((routes) => {
	console.log(inspect(routes, {depth: null}))
})
.catch((err) => {
	console.error(err)
	process.exit(1)
})
