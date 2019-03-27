var count = 0;
var count2 = 0;
$(function() {
    $("#textarea").keypress(function (e) {
        if(e.which == 13) {
            var input = $('#textarea').val();
            console.log(input)
            $(this).val("");
            e.preventDefault();
            document.getElementById("chatbox").innerHTML += "<div>Vous : " + input + "<br></div>";
            document.getElementById("chatbox").innerHTML += '<img id="ajax-loading'+count2+'" src="http://loadinggif.com/generated-image?imageId=31&bgColor=%23ccc&fgColor=%23000000&transparentBg=0&download=0&random=0.00030365096131301783" />';
            $('#ajax-loading'+count2).show();
            $.get('../map?value='+input, function(reponse) {
                if (reponse == 'GrandPy : Je ne vois pas de quel endroit tu parles') {
                    $('#ajax-loading'+count2).hide();
                    document.getElementById("chatbox").innerHTML += "<div>" + reponse + "<br></div>";
                } else {
                    reponse = JSON.parse(reponse);
                    name = reponse[0][0];
                    lat = parseFloat(reponse[0][1]);
                    lon = parseFloat(reponse[0][2]);
                    $('#ajax-loading'+count2).hide();
                    document.getElementById("chatbox").innerHTML += "<div>GrandPy : Bien sûr mon poussin ! La voici : " + name + "<br></div>";
                    document.getElementById("chatbox").innerHTML += '<div class="map" id="mapid' + count + '"></div>';
                    document.getElementById("chatbox").innerHTML += "<div>" + reponse[1] + "<br></div>";        
                    var mymap = L.map('mapid'+count).setView([lat, lon], 15);
                    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                        maxZoom: 18,
                        id: 'mapbox.streets',
                        accessToken: 'pk.eyJ1IjoiLS0tbWF4LS0tIiwiYSI6ImNqc2o1N3puYjF1N3k0NHFnNDNyMnQycnMifQ.uSomfCplZE4eR-znItMviQ'
                    }).addTo(mymap);
                    var marker = L.marker([lat, lon]).addTo(mymap);
                    count ++;
                }
                count2 ++;
            })
        }
    });
});