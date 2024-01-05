const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer({});
const port = 80;
const targetPort = 8080;  // 這是您的應用程序實際運行的端口

http.createServer((req, res) => {
  proxy.web(req, res, { target: `http://127.0.0.1:${targetPort}` });
}).listen(port);