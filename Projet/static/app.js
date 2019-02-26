$('#send').click(function() {
    var input = $('#textarea').val()
    document.getElementById("chatbox").innerHTML += "Vous : " + input + "<br>";
    $.get('http://127.0.0.1:5000/test?value='+input, function(reponse) {
        reponse = JSON.parse(reponse)
        lat = parseFloat(reponse[1])
        lon = parseFloat(reponse[2])
        var mymap = L.map('mapid').setView([lat, lon], 15);
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.streets',
            accessToken: 'pk.eyJ1IjoiLS0tbWF4LS0tIiwiYSI6ImNqc2o1N3puYjF1N3k0NHFnNDNyMnQycnMifQ.uSomfCplZE4eR-znItMviQ'
        }).addTo(mymap);
        var marker = L.marker([lat, lon]).addTo(mymap);
    })
})
