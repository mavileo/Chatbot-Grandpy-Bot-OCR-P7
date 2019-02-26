var count = 0
$('#send').click(function() {
    var input = $('#textarea').val()
    document.getElementById("chatbox").innerHTML += "<div>Vous : " + input + "<br></div>";
    $.get('http://127.0.0.1:5000/test?value='+input, function(reponse) {
        reponse = JSON.parse(reponse);
        name = reponse[0];
        lat = parseFloat(reponse[1]);
        lon = parseFloat(reponse[2]);
        document.getElementById("chatbox").innerHTML += "<div>GrandPy : Bien sûr mon poussin ! La voici : " + name + "<br></div>";
        document.getElementById("chatbox").innerHTML += '<div class="map" id="mapid' + count + '"></div>';
        var mymap = L.map('mapid'+count).setView([lat, lon], 15);
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.streets',
            accessToken: 'pk.eyJ1IjoiLS0tbWF4LS0tIiwiYSI6ImNqc2o1N3puYjF1N3k0NHFnNDNyMnQycnMifQ.uSomfCplZE4eR-znItMviQ'
        }).addTo(mymap);
        var marker = L.marker([lat, lon]).addTo(mymap);
        count ++;
    })
})

