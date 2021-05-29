function getCoordinates(place) {
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"+ place +".json?access_token=pk.eyJ1IjoiYWJoaWttcCIsImEiOiJja2phM2xjZDQ3N214MnFsYm9icWFidWRpIn0.xpSSYysroFrKHyZcTBFcVw";
    fetch(url).then(data => {return data}).then(res => {console.log(res)}).catch(err => {console.log(err)});
}

getCoordinates('chengannur');