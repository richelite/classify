function settings() {
	this.url = 'http://api.yhathq.com/predict?';
	this.mood =  { 
            username: 'username',
            model: 'classifiername',
            version: 1,
            apikey: 'apikey' 
	}
	this.political = { 
            username: 'username',
            model: 'classifiername',
            version: 1,
            apikey: 'apikey'  
	}
};

module.exports = settings;