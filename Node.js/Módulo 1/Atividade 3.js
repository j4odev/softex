    var request = require('request');
 function updateClient(postData){
            var clientServerOptions = {
                uri: 'http://'+clientHost+''+clientContext,
                body: JSON.stringify(postData),
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            request(clientServerOptions, function (error, response) {
                console.log(error,response.body);
                return;
            });
        }
// Para funcionar, deve-se fazer:

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json())

var port = 8080;

app.post('/sample/put/data', function(req, res) {
    console.log('receiving data ...');
    console.log('body is ',req.body);
    res.send(req.body);
});

// start the server
app.listen(port);
console.log('Server started! At http://localhost:' + port);
