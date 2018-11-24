var entered_url = "";
var score = 0;
var server = "http://localhost:3000"

function calculate_fake_news_score() {
	entered_url = document.getElementById("url").value;
	console.log("ENTERED URL: " + entered_url);


	// TODO: change to entered_url
	fetch(entered_url)
  		.then(function(response) {
    		return response.json();
 	 	})
  		.then(function(myJson) {
  			console.log(JSON.stringify(myJson));
  			// parse JSON response from esp
   	 		var obj = JSON.parse(myJson);
   	 		score = parseInt(obj.score, 10);
  		});

  	// set the text label
  	document.getElementById("result").value = "hey";
}


window.onload = function() {

}

