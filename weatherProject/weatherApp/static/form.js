document.addEventListener('DOMContentLoaded', function() {
    function initialize() {
        var input = document.getElementById('cityInput');
        var options = {
            types: ['(cities)']
        };
        var autocomplete = new google.maps.places.Autocomplete(input, options);
    }
    google.maps.event.addDomListener(window, 'load', initialize);
})