Classifier = new Meteor.Collection('classifier');

if (Meteor.is_client) {
  var userName = "richeliteys";
  Template.hello.greeting = function () {
    return "Fetch recent tweets from Twitter stream of user : " ;
  };
 
  Template.hello.events = {
    'keydown #userName' : function () {
      var userName = $('#userName').val();
      var now = new Date();
      Meteor.call('fetchFromService', userName, function(err, respJson) {
        if(err) {
          window.alert("Error: " + err.reason);
          console.log("error occured on receiving data on server. ", err );
        } else {
          respJson.forEach(function(item){
            Meteor.call('classifyMood', item.text, function(err, res) {
              if(err) {
                window.alert("Error: " + err.reason);
                console.log("error occured on receiving data on server. ", err );
              } else {
                console.log("respJson: ", res);
                // Session.set("recentTweets",respJson);
                if (res == '1') cls = 'positive';
                else cls = 'negative';
                Classifier.insert({
                  text: item.text,
                  class: cls,
                  tweettime: item.created_at,
                  clftime: now
                });
              }
            });
          });
          // Session.set("recentTweets",respJson);
        }
      });
    }
  };
  
  Template.hello.recentTweets = function() {
    // return Session.get("recentTweets") || [];
    return Classifier.find({}, { sort: { clftime: -1 }});
  }
  
  Template.hello.userName = function() {
    return userName;
  }
}
 
if (Meteor.is_server) {
  Classifier.remove({});
  var yhurl = 'http://api.yhathq.com/predict?' 
  serialize = function(obj) {
    var str = [];
    for(var p in obj)
       str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    return str.join("&");
  }
  Meteor.methods({
    fetchFromService: function(userName) {
      var twurl = "https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name="+userName+"&count=15";
      //synchronous GET
      var result = Meteor.http.get(twurl);
      if(result.statusCode==200) {
        var respJson = JSON.parse(result.content);
        console.log("response received.");      
        return respJson;
      } else {
        console.log("Response issue: ", result.statusCode);
        var errorJson = JSON.parse(result.content);
        throw new Meteor.Error(result.statusCode, errorJson.error);
      }
    },
    classifyMood: function(message) {
      var yhat = { username: 'yangshuo@umich.edu',
                 model: 'MoodSVMClassifier',
                 version: 1,
                 apikey: 'yWsCVKWFdXcbXrCArSq4pxCjRMEqcuONZp2AsgOidl0' }
      data = {"data": message};
      data = JSON.stringify(data);
      //synchronous POST
      var result = Meteor.http.post(yhurl + serialize(yhat), {content:data, headers: { "Content-Type": "application/json"}});
      if(result.statusCode==200) {
        var respJson = JSON.parse(result.content);
        console.log("response received.");      
        return respJson.prediction.probabilities;
      } else {
        console.log("Response issue: ", result.statusCode);
        var errorJson = JSON.parse(result.content);
        throw new Meteor.Error(result.statusCode, errorJson.error);
      }
    }
  });

}