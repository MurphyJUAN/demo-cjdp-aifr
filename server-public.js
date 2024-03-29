


// Run on aifr server
const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');
const port = 443
const app = express();


// the __dirname is the current directory from where the script is running
// app.use(express.static(__dirname + '/dist'));

const staticFileMiddleware = express.static(__dirname + '/dist');
app.use(staticFileMiddleware);
app.use(history({
disableDotRule: true,
verbose: true
}));
app.use(staticFileMiddleware);




// send the user to index html page inspite of the url
app.get('*', (req, res) => {
res.sendFile(path.resolve(__dirname, 'index.html'));
});

app.listen(port);
