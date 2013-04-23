Positive = new Meteor.Collection('Positive');
Negative = new Meteor.Collection('Negative');


if (Meteor.is_client) {
  Template.messageP.message = function(){
    return Positive.find({}, { sort: { clfTime: -1 }});
  }
  Template.Pcount.count = function(){
    return Positive.find({}).count();
  }
  Template.messageN.message = function(){
    return Negative.find({}, { sort: { clfTime: -1 }});
  }
  Template.Ncount.count = function(){
    return Negative.find({}).count();
  }
  Template.userNameEntry.events = {
    'click #classify' : function () {
      var userName = $('#userNameInput').val();
      if (userName == ''){
        window.alert("Error: empty username");
      }
      else {
        $('#classify').attr('disabled','true').val('loading...');
        var now = new Date();
        var utc = now.toUTCString();
        var now = utc.split(', ')[1];
        Meteor.call('fetchFromService', userName, function(err, respJson) {
          if(err) {
            window.alert("Error: " + err.reason);
            $('#classify').removeAttr('disabled').val('Classify');
            console.log("error occured on receiving data on server. ", err );
          } else {
            respJson.forEach(function(item){
              console.log(item);
              Meteor.call('classifyMood', item.text, function(err, res) {
                if(err) {
                  window.alert("Error: " + err.reason);
                  console.log("error occured on receiving data on server. ", err );
                } else {
                  console.log("respJson: ", res);
                  // Session.set("recentTweets",respJson);
                  timeSplit = item.created_at.split(' ');
                  tweetTime = timeSplit[1]+' '+timeSplit[2]+' '+timeSplit[5];
                  if (res == '1') {
                    Positive.insert({
                      text: item.text,
                      tweetTime: tweetTime,
                      user: item.user.screen_name,
                      img: item.user.profile_image_url,
                      clfTime: now
                    });
                  }
                  else {
                    Negative.insert({
                      text: item.text,
                      tweetTime: tweetTime,
                      user: item.user.screen_name,
                      img: item.user.profile_image_url,
                      clfTime: now
                    });
                  };
                  $('#userNameInput').val('');
                  $('#classify').removeAttr('disabled').val('Classify');
                }
              });
            });
          }
        });
      }
    }
  };
}
 
if (Meteor.is_server) {
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