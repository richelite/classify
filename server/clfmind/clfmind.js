Positive = new Meteor.Collection('Positive');
Negative = new Meteor.Collection('Negative');


if (Meteor.is_client) {
  Template.messageP.message = function(){
    return Positive.find({}, { sort: { time: -1 }});
  }
  Template.messageN.message = function(){
    return Negative.find({}, { sort: { time: -1 }});
  }

  Template.messageEntry.events = {
    "keydown #messageInput": function(event){
      if(event.which == 13){
        // Submit the form
        var message = $('#messageInput');
        var messageValue = $('#messageInput').val();
        var now = new Date();
        var now = now.toLocaleString();
        if(messageValue == ''){
          window.alert("Error: Empty value");
          message.val('');
        }
        else{
          Meteor.call('classifyPolitics', messageValue, function(err, respJson) {
            if(err) {
              window.alert("Error: " + err.reason);
              console.log("error occured on receiving data on server. ", err );
            } else {
              console.log("respJson: ", respJson);
              // Session.set("recentTweets",respJson);
              if (respJson == '1') {
                Positive.insert({
                  content: messageValue,
                  class: respJson,
                  time: now
                });
              }
              else {             
                Negative.insert({
                  content: messageValue,
                  class: respJson,
                  time: now
                });
              }
              message.val('');
            }           
          });
        }
      }
    }
  }
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
    classifyPolitics: function(message) {
      var yhat = { username: 'richeliteys@gmail.com',
                 model: 'PoliticalSVMClassifier',
                 version: 1,
                 apikey: 'RoVGt5VDZfHkdBLx2rre76sg998cD4IuJiYzzNmNp48' }
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