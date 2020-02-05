{"changed":true,"filter":false,"title":"server.py","tooltip":"/hbs/public/personal_portfolio/server.py","value":"var http = require('http');\nvar fs = require('fs');\nvar url = require('url');\n\nhttp.createServer( function (request, response) {\n  var pathname = url.parse(request.url).pathname;\n  console.log(\"Trying to find '\" + pathname.substr(1) + \"'...\");\n\n  fs.readFile(pathname.substr(1), function (err, data) {\n    if (err) {\n      response.writeHead(404, {'Content-Type': 'text/html'});\n      response.write(\"ERROR: Cannot find '\" + pathname.substr(1) + \"'.\");\n      console.log(\"ERROR: Cannot find '\" + pathname.substr(1) + \"'.\");\n    } else {\n      console.log(\"Found '\" + pathname.substr(1) + \"'.\");\n      response.writeHead(200, {'Content-Type': 'text/html'});\n      response.write(data.toString());\n    }\n    response.end();\n  });\n}).listen(8080, 'localhost'); // Or 8081 or 8082 instead of 8080. Or '127.0.0.","undoManager":{"mark":0,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":21},"action":"insert","lines":["import os","import SimpleHTTPServer","import SocketServer","","ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.","port = '8080' # Or '8081' or '8082' instead of '8080'.","Handler = SimpleHTTPServer.SimpleHTTPRequestHandler","httpd = SocketServer.TCPServer((ip, int(port)), Handler)","httpd.serve_forever()"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":21},"action":"remove","lines":["import os","import SimpleHTTPServer","import SocketServer","","ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.","port = '8080' # Or '8081' or '8082' instead of '8080'.","Handler = SimpleHTTPServer.SimpleHTTPRequestHandler","httpd = SocketServer.TCPServer((ip, int(port)), Handler)","httpd.serve_forever()"],"id":2},{"start":{"row":0,"column":0},"end":{"row":20,"column":78},"action":"insert","lines":["var http = require('http');","var fs = require('fs');","var url = require('url');","","http.createServer( function (request, response) {","  var pathname = url.parse(request.url).pathname;","  console.log(\"Trying to find '\" + pathname.substr(1) + \"'...\");","","  fs.readFile(pathname.substr(1), function (err, data) {","    if (err) {","      response.writeHead(404, {'Content-Type': 'text/html'});","      response.write(\"ERROR: Cannot find '\" + pathname.substr(1) + \"'.\");","      console.log(\"ERROR: Cannot find '\" + pathname.substr(1) + \"'.\");","    } else {","      console.log(\"Found '\" + pathname.substr(1) + \"'.\");","      response.writeHead(200, {'Content-Type': 'text/html'});","      response.write(data.toString());","    }","    response.end();","  });","}).listen(8080, 'localhost'); // Or 8081 or 8082 instead of 8080. Or '127.0.0."]}]]},"ace":{"folds":[],"customSyntax":"javascript","scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":78},"end":{"row":20,"column":78},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1580700258212}