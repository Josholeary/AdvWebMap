let area;

map = L.map('map').fitWorld();

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

map.locate({setView: true, maxZoom: 16});


let Picon = L.icon({
    iconUrl: bike,
    iconSize: [50, 50],
});

fetch(bp)
    .then(function (resp){
        return resp.json();
    }).then(function (data){
        L.geoJson(data, {
            onEachFeature: function (feature, layer){
            layer.bindPopup(feature.properties.operator);
            },
        }).addTo(map);
});




// https://leafletjs.com/examples/mobile/

function onLocationFound(event) {
    let position = event.latlng;
    let lat = position.lat;
    let lon = position.lng;
    let rad = event.accuracy / 2;
    let coord =  "| Your position is - " + "Longitude:" + lon + " Latitude:" + lat + " |";
    document.getElementById('coordinates').innerHTML = coord;
    let popbox = "Your location is within: " + rad+"M";
    area = L.circle(position, rad).addTo(map);
    let marker = L.marker(position, {icon: Picon}).addTo(map);
    marker.bindPopup(popbox).openPopup();
    marker.getPopup().setContent(popbox);
    marker.setLatLng(position);

    // trigger json response for url of add_location_db which will activate view.py function saving to profile
    fetch('/add_location_db/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'latitude': lat, 'longitude': lon})
    })
        .then((response) => {
            return response.json()
        })
}



map.on('locationfound', onLocationFound);
