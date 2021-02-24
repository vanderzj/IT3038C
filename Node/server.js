var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");

//Gets host uptime and formats it.
var sec = os.uptime();
var min = sec/60;
var hr = min/60;
var day = hr/24;

sec = Math.floor(sec);
min = Math.floor(min);
hr = Math.floor(hr);
day = Math.floor(day);

sec = sec%60;
min = min%60;
hr = hr%24;

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`
        <!DOCTYPE html>
         <html>
          <head>
           <title>Node JS Response</title>
          </head>
          <body>
           <p>Hostname: ${myHostName}</p>
           <p>IP: ${ip.address()}</p>
           <p>Server Uptime: ${day} days, ${hr} hours, ${min} minutes, and ${sec} seconds.</p>
           <p>Total Memory: ` + os.totalmem()/1000000 + ` MB</p>
           <p>Free Memory: ` + os.freemem()/1000000 + ` MB</p>
           <p>Number of CPUs: ` + os.cpus().length + `  </p>
          </body>
         </html>`
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html)
    }
    
    else {
        res.writeHead(404, {"Content-Type": "test/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");