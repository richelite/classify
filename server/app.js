var express = require('express')
  , http = require('http')
  , request = require('request')
  , async = require('async')
  , path = require('path')
  , Settings = require('./settings');

var app = express();
var settings = new Settings();

app.configure(function(){
    app.set('port', process.env.PORT || 3000);
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.use(express.favicon());
    app.use(express.logger('dev'));
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(express.static(path.join(__dirname, 'public')));
});

app.get('/', function(req,res){
    res.render('index', { value: '', message: '' });
})

app.post('/', function(req,res){
    text_message = req.body.classify
    if (text_message=='') {
        res.render('index', { value: text_message, message: 'Are you meditating?' });
    }
    else {
    data = { "data": text_message }
        async.series([
            function(callback){
                request.post(
                    {   
                        url: settings.url + serialize(settings.mood),
                        headers: {
                        "Content-Type": "application/json"
                        },
                        body: JSON.stringify(data),
                        json: true,
                    },
                    function (error, response, data) {
                        callback(null, data.prediction.probabilities);  
                    });
            },
            function(callback){
                request.post(
                    {   
                        url: settings.url + serialize(settings.political),
                        headers: {
                        "Content-Type": "application/json"
                        },
                        body: JSON.stringify(data),
                        json: true,
                    },
                    function (error, response, data) {
                        callback(null, data.prediction.probabilities);  
                    });
            }
        ],
        function(err, results){
            var result = '';
            switch (results.toString())
            {
                case '1,1':
                    result = 'You were talking about politics. And you like it!'
                    break;
                case '1,0':
                    result = 'You were not talk about politics! And you like it!'
                    break;
                case '0,1':
                    result = "You were talking about politics. And you don' like it!"
                    break;
                case '0,0':
                    result = "You were not talking about politics. And you don' like it!"
                    break;
            }
            res.render('index', { value: text_message, message: result });
        });
    }

});

serialize = function(obj) {
    var str = [];
    for(var p in obj)
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    return str.join("&");
}

http.createServer(app).listen(app.get('port'), function(){
    console.log("Express server listening on port " + app.get('port'));
});