// fetches tweets from database and injects into html
function write_tweets() {$.getJSON('/tweets',
		function (tweets) {
			if (tweets) {
				var html = '<ul class="list-group">';
				$.each(tweets, function(i, tweet) {
					html += '<li class="list-group-item"> <strong>' + tweet.fields.user + '</strong>: '
					html += tweet.fields.text + ' (' + tweet.fields.lat + ',' + tweet.fields.lon + ')</li>'
				});
				html += '</ul>'
				$('#tweets .container-fluid #tweet').html(html);
			}
		}
	);
}

// fetches tweets from database and injects into html
function plot_tweets() {$.getJSON('/tweets',
		function (tweets) {
			$.each(tweets, function(i, tweet) {
				var lat = tweet.fields.lat;
				var lon = tweet.fields.lon;
				map.plot(lon, lat);
			});
		}
	);
}

// updates tweets at <rate> time intervals (milliseconds)
function tweetstream(rate) {
	setInterval(function () {
		plot_tweets();
	}, rate);
}

// creates svg map
var MapWidth = 800;
var container = 'map';
var paper = new ScaleRaphael(container, 950, 650);
var map = paper.USMap();
paper.scaleAll(MapWidth/map.width);
tweetstream();

//map.darkenState('PA', 1.07);
