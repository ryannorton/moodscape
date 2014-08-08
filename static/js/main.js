// fetches tweets from database and injects into html
function get_tweets(start, n) {$.getJSON('/tweets/' + start + '/' + n,
		function (tweets) {
			if (tweets) {
				// write tweets
				var html = '<ul class="list-group">';
				$.each(tweets.slice(0,5), function(i, tweet) {
					html += '<li class="list-group-item"> <strong>' + tweet.fields.user + '</strong>: ('
					html += tweet.fields.sentiment + ') ' + tweet.fields.text + ' (' + tweet.fields.lat + ',' + tweet.fields.lon + ')</li>'
				});
				html += '</ul>'
				$('#tweets #tweet').html(html);

				// map tweets
				$.each(tweets, function(i, tweet) {
					console.log(tweet);
					var lat = tweet.fields.lat;
					var lon = tweet.fields.lon;
					map.plot(lon, lat, tweet.fields.user + ': ' + tweet.fields.text, tweet.fields.url);
					var coords = LatLonToHeat(lon, lat);
					heatmap.addData({
						x: coords[0],
						y: coords[1],
						value: tweet.fields.sentiment,
					});
				});
			}
		}
	);
}

// fetches tweets from database and plots on map and heatmap
function plot_tweets() {$.getJSON('/tweets',
		function (tweets) {
			$.each(tweets, function(i, tweet) {
				var lat = tweet.fields.lat;
				var lon = tweet.fields.lon;
				map.plot(lon, lat, tweet.fields.user + ': ' + tweet.fields.text, tweet.fields.url);
				var coords = LatLonToHeat(lon, lat);
				heatmap.addData({
					x: coords[0],
					y: coords[1],
					value: tweet.fields.sentiment,
				});
			});
		}
	);
}

// updates tweets at <rate> time intervals (milliseconds)
function tweetstream(rate) {
	setInterval(function () {
		plot_tweets();
		write_tweets();
	}, rate);
}

function LatLonToHeat(lat, lon) {
    var xOffset = -17;
    var yOffset = -22;
    var scaleX = 10.05;
    var scaleY = 6.26;
    var i = 0.842;

    var x = 50.0 + 124.03149777329222 * ((1.9694462586094064-(lat* Math.PI / 180)) * Math.sin(0.6010514667026994 * (lon + 96) * Math.PI / 180));
    var y = 50.0 + 1.6155950752393982 * 124.03149777329222 * 0.02613325650382181 - 1.6155950752393982  * 124.03149777329222 * (1.3236744353715044  - (1.9694462586094064-(lat* Math.PI / 180)) * Math.cos(0.6010514667026994 * (lon + 96) * Math.PI / 180));
  	return([((x * scaleX + xOffset) * i), ((y * scaleY + yOffset) * i)]);
}

// creates svg map
var MapWidth = 800;
var container = 'map';
var paper = new ScaleRaphael(container, 950, 650);
var map = paper.USMap();
paper.scaleAll(MapWidth/map.width);

// creates heatmap overlay
var heatmap = h337.create({container: document.getElementById('map'), radius: 40});
heatmap.setDataMax(1.0);
heatmap.setDataMin(-1.0);

function doSetTimeout(i) {
	setTimeout(function () {
		get_tweets(i*500, 500);
	}, i*2000);
}

for (var i = 0; i<90; i++) {
	doSetTimeout(i);
}

