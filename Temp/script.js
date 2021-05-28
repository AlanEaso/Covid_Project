mapboxgl.accessToken = 'pk.eyJ1IjoiYWJoaWttcCIsImEiOiJja2phM2xjZDQ3N214MnFsYm9icWFidWRpIn0.xpSSYysroFrKHyZcTBFcVw'
const map = new mapboxgl.Map({
   container: 'map',
   style: 'mapbox://styles/mapbox/streets-v10',
   center: [76.6144355, 9.3175825],
   zoom: 8,

});

var bounds = [[76.5617, 9.2177],[76.6710,9.3690]];
map.setMaxBounds(bounds);
var canvas = map.getCanvasContainer();
var start = document.getElementById('start');
var end = document.getElementById('end');
console.log(start);
console.log(end);

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, ({enableHighAccuracy: True}));

if (start = "") {
    navigator.geolocation.getCurrentPosition(successLocation, errorLocation);    
}else{
    successLocation(getCoordinates(start));
}

function successLocation(position){
    start = position;
    console.log(start);
}

function errorLocation(){
    console.log("error in finding location. please try again enabling your location settings.");
}




function getCoordinates(){
    var url = "https://api.mapbox.com/geocoding/v5/mapbox.places/chengannur.json?bbox=76.5617,9.2177,76.6710,9.3690&access_token="+mapboxgl.accessToken;
    fetch(url).then(data => {return data.json()}).then(response => {console.log(response)}).catch(error => {console.log(error)});
}