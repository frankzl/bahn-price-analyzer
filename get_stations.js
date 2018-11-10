const stations = require('db-stations')

stations()
    .on('data', function(data){
        // console.log("{name: \"" + data.name + "\", id: "+data.id + "},")
        console.log(data)
    })
    .on('error', console.error)
