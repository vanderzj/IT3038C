var config = require('config')
var express = require('express')
var app = express()
//var fs = require('fs')

//var file = fs.readFileSync('./Public/widgets.json', 'utf-8')

app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/name', function(request, response) {
  if(config.util.getEnv("MY_NAME") === "Zack"){
    response.send("<b>Hello, my name is " +  + process.env.MY_NAME + "</b>")
  }
  else{
    response.send("<b>No name found</b>")
  }
})

app.get('/api', function(request, response) {
  //response.send("<b>" + file + "</b>")
})

app.get('/', function(request, response) {
  if(config.util.getEnv("NODE_ENV") === "Testing"){
    response.send("<b>You are working in the Testing environment.</b>")
  }
  else if(config.util.getEnv("NODE_ENV") === "HerokuTest"){
    response.send("<b>You are working in the HerokuTest environment.</b>")
  }
  else if(config.util.getEnv("NODE_ENV") === "Production"){
    response.send("<b>You are working in the Production environment.</b>")
  }
  else{
    response.send("<b>Environment Unknown</b>")
  }
  //response.send('Hello World! My name is <em>' + process.env.MYNAME + '</em> <br /> My Node Evironment is: ' + webkitConvertPointFromPageToNode.util.getEnv('NODE_ENV') + "</b>")
})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
