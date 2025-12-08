window.addEventListener('load', function () {
    load_map_data();
    document.querySelector('div.leaflet-control-attribution').remove();
})

function load_map_data() {
    let marker;
    let lat = document.getElementById('coords_lat_input').value;
    let lng = document.getElementById('coords_lng_input').value;
    map = L.map('map').setView([lat, lng], 15);
    marker = L.marker([lat, lng]).addTo(map);
    let layer_1 = L.tileLayer('https://tile.jawg.io/jawg-streets/{z}/{x}/{y}{r}.png?access-token=DpsH4dBaam2j9LC9TfSXdJbKsqcfPqAz69VY2tTecW1bMehuoysQvH9uNUnCEBj0', {
        attribution: '<a href="http://jawg.io" target="_blank">&copy; Jawg</a> &copy; OSM',
        maxZoom: 22
    });
    let layer_2 = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
    });
    let baseMaps = {
        "layer 1": layer_1,
        "layer 2": layer_2,
    };
    layer_1.addTo(map);
    L.control.layers(baseMaps).addTo(map);
}