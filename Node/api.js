var data = require("./Public/data/widgets.json");
var http = require("http");

function listBlue(res) {
    var colorBlue = data.filter(function(item){
        return item.color === "Blue";
    });

    res.end(JSON.stringify(colorBlue))
}

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));
    }
    
    else if (req.url === "/blue") {
        listBlue(res);
    }

    else {
        res.writeHead(404, {"Content-Type": "test/plain"});
        res.end(`Data not found.`);
    }
});

server.listen(3000);
console.log("Server listening on port 3000");