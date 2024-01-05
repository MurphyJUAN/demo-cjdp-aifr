/**
 * File: /media/allenyl/DATA/Projects/server_setup/repo-ai/nlp-judgement-frontend/server.js
 * Project: /media/allenyl/DATA/Projects/server_setup/repo-ai/nlp-judgement-frontend
 * Created Date: Friday, September 13th 2019, 12:57:46 pm
 * Author: Allenyl(allen7575@gmail.com>)
 * -----
 * Last Modified:
 * Modified By:
 * -----
 * Copyright 2018 - 2019 Allenyl Copyright, Allenyl Company
 * -----
 * license:
 * All shall be well and all shall be well and all manner of things shall be well.
 * We're doomed!
 * ------------------------------------
 * HISTORY:
 * Date      	By	Comments
 * ----------	---	---------------------------------------------------------
 */


const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');
const port = process.env.PORT || 8080;
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