const prices = require('db-prices')

const moment = require('moment-timezone')
const {inspect} = require('util')

const tz = 'Europe/Berlin'
// some monday in the future
const when = moment.tz(Date.now(), tz).hour(10).minute(30).second(0).day(1 + 7).toDate()

console.log(when.getDay())
console.log(when.getMonth())
console.log(when.getYear())
