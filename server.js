var http = require('http'),
    fs = require('fs'),
    path = require('path');

var Finder = require('fs-finder');
var exec = require('child_process').exec;
var search = require('recursive-search');
var config = JSON.parse(fs.readFileSync(__dirname+"/config.json"));

http.createServer(function(req, res) {
    var results = [];

    var results = [];
    while (!results.length) {
        var results = search.recursiveSearchSync('track01.wav', __dirname);
        try {
            var wavFile = results[0];
        } catch (e) {
            var wavFile;
        }
    }

    var range = req.headers.range;
    var totalSize = 1024 * 1024 * 1024 * 5;
    var start = 0;
    headers = {
        'Content-Length': totalSize,
        'Content-Type': 'audio/wav'
    };
    res.writeHead(200, headers);
    var filestream = fs.createReadStream(wavFile, {start, totalSize});
    filestream.pipe(res);
}).listen(config.public_port);
