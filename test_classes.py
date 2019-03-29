"""This file contains tests"""

import requests
import classes

def test_map1(monkeypatch):
    data = [{'place_id': '247332235', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '6242758322', 'boundingbox': ['48.8747286', '48.8748286', '2.3504385', '2.3505385'], 'lat': '48.8747786', 'lon': '2.3504885', 'display_name': 'OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', 'class': 'office', 'type': 'company', 'importance': 0.101}]
    result = ['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885', 'Cité Paradis', 'Paris']
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.request_map('OpenClassrooms') == result

def test_map2(monkeypatch):
    data = [{'place_id': '93566511', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'way', 'osm_id': '56185523', 'boundingbox': ['48.8650731', '48.8672298', '2.3111783', '2.3133551'], 'lat': '48.86616135', 'lon': '2.31222295966943', 'display_name': 'Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', 'class': 'tourism', 'type': 'museum', 'importance': 0.61742491162142, 'icon': 'https://locationiq.org/static/images/mapicons/tourist_museum.p.20.png'}, {'place_id': '209793467', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'relation', 'osm_id': '7483660', 'boundingbox': ['59.8841083', '59.8849316', '29.9063888', '29.9112836'], 'lat': '59.8845122', 'lon': '29.9092348004647', 'display_name': 'Grand Palace, Avenue of the fountains, Skorokhod, Peterhof, Петродворцовый район, Saint Petersburg, Northwestern Federal District, 190000, Russia', 'class': 'tourism', 'type': 'museum', 'importance': 0.46816821007254, 'icon': 'https://locationiq.org/static/images/mapicons/tourist_museum.p.20.png'}, {'place_id': '63454943', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '5337116251', 'boundingbox': ['48.29578', '48.31578', '4.7521532', '4.7721532'], 'lat': '48.30578', 'lon': '4.7621532', 'display_name': 'Le Grand Palais, Fresnay, Bar-sur-Aube, Aube, Grand Est, Metropolitan France, 10200, France', 'class': 'place', 'type': 'locality', 'importance': 0.45, 'icon': 'https://locationiq.org/static/images/mapicons/poi_place_village.p.20.png'}, {'place_id': '16169425', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '1504098202', 'boundingbox': ['48.866585', '48.866685', '2.3098631', '2.3099631'], 'lat': '48.866635', 'lon': '2.3099131', 'display_name': 'Le Grand Palais, Rue Jean Goujon, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', 'class': 'amenity', 'type': 'restaurant', 'importance': 0.201, 'icon': 'https://locationiq.org/static/images/mapicons/food_restaurant.p.20.png'}, {'place_id': '8313211', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '911471125', 'boundingbox': ['48.8653699', '48.8654699', '2.3135131', '2.3136131'], 'lat': '48.8654199', 'lon': '2.3135631', 'display_name': 'Grand Palais, Avenue Winston Churchill, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', 'class': 'highway', 'type': 'bus_stop', 'importance': 0.201, 'icon': 'https://locationiq.org/static/images/mapicons/transport_bus_stop2.p.20.png'}, {'place_id': '20062405', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '2042462230', 'boundingbox': ['48.8649914', '48.8650914', '2.3129643', '2.3130643'], 'lat': '48.8650414', 'lon': '2.3130143', 'display_name': 'Grand Palais, Cours la Reine, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', 'class': 'highway', 'type': 'bus_stop', 'importance': 0.201, 'icon': 'https://locationiq.org/static/images/mapicons/transport_bus_stop2.p.20.png'}, {'place_id': '248753801', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '6283856612', 'boundingbox': ['48.8683194', '48.8684194', '2.3165622', '2.3166622'], 'lat': '48.8683694', 'lon': '2.3166122', 'display_name': 'Grand Palais, Avenue Gabriel, Madeleine, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', 'class': 'highway', 'type': 'bus_stop', 'importance': 0.201, 'icon': 'https://locationiq.org/static/images/mapicons/transport_bus_stop2.p.20.png'}, {'place_id': '122118510', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'way', 'osm_id': '182431440', 'boundingbox': ['45.49582', '45.4962424', '-73.8528431', '-73.8520538'], 'lat': '45.49603125', 'lon': '-73.8524484439377', 'display_name': 'Le Grand Palais, 160, Chemin de la Rive-Boisée, Pierrefonds-Roxboro, Montreal, Urban agglomeration of Montreal, Montreal (06), Quebec, H8Z 3L2, Canada', 'class': 'building', 'type': 'apartments', 'importance': 0.201}, {'place_id': '114796015', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'way', 'osm_id': '154792666', 'boundingbox': ['43.2713658', '43.272476', '5.397094', '5.3981257'], 'lat': '43.27189475', 'lon': '5.39763336175236', 'display_name': "Grand Palais, Allée Ray-Grassi, Saint-Giniez, 8th arrondissement of Marseille, Marseille, Bouches-du-Rhône, Provence-Alpes-Côte d'Azur, Metropolitan France, 13008, France", 'class': 'building', 'type': 'commercial', 'importance': 0.201}, {'place_id': '50228435', 'licence': 'https://locationiq.com/attribution', 'osm_type': 'node', 'osm_id': '3891932251', 'boundingbox': ['50.6301781', '50.6302781', '3.0773733', '3.0774733'], 'lat': '50.6302281', 'lon': '3.0774233', 'display_name': 'Grand Palais, Avenue du Président Hoover, Mont de Terre, Lille, Nord, Nord-Pas-de-Calais and Picardy, Metropolitan France, 59042, France', 'class': 'amenity', 'type': 'car_sharing', 'importance': 0.201}]
    result = ['Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.86616135', '2.31222295966943', 'Avenue du Général Eisenhower', 'Paris']
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.request_map('OpenClassrooms') == result

def test_getpageid1(monkeypatch):
    data = {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 4680}, 'search': [{'ns': 0, 'title': 'Cité Paradis', 'pageid': 5653202, 'size': 2777, 'wordcount': 232, 'snippet': 'homonymes, voir <span class="searchmatch">Paradis</span> (homonymie). La <span class="searchmatch">cité</span> <span class="searchmatch">Paradis</span> est une voie publique située dans le 10e\xa0arrondissement de Paris. La <span class="searchmatch">cité</span> <span class="searchmatch">Paradis</span> est une voie publique', 'timestamp': '2018-08-08T11:50:07Z'}, {'ns': 0, 'title': 'OpenClassrooms', 'pageid': 4338589, 'size': 31062, 'wordcount': 3218, 'snippet': '9e\xa0rue le Peletier, puis au boulevard Haussmann et enfin dans Paris 10e <span class="searchmatch">cité</span> <span class="searchmatch">Paradis</span> en 2014,. L\'actionnariat s\'étend en février 2012 avec l\'arrivée au capital', 'timestamp': '2019-03-29T08:04:55Z'}, {'ns': 0, 'title': 'Paradis', 'pageid': 1320354, 'size': 38354, 'wordcount': 5224, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Paradis</span> (homonymie). Le <span class="searchmatch">paradis</span> ou jardin d\'Éden représente souvent le lieu final où les humains seront récompensés', 'timestamp': '2019-03-28T02:46:17Z'}, {'ns': 0, 'title': 'Baden-Baden', 'pageid': 101193, 'size': 26605, 'wordcount': 2974, 'snippet': 'usuellement désignées sous le nom collectif de «\xa0Stadtteil <span class="searchmatch">Cité</span>\xa0». L\'ancienne «\xa0<span class="searchmatch">Cité</span> <span class="searchmatch">Paradis</span>\xa0» (qui tirait son nom de la Paradiesstraße), qui abritait', 'timestamp': '2019-01-13T18:48:18Z'}, {'ns': 0, 'title': 'Liste des voies du 10e arrondissement de Paris', 'pageid': 3134775, 'size': 7521, 'wordcount': 645, 'snippet': 'Monseigneur-Rodhain Rue de Nancy Place Napoléon-III Place du 11-Novembre-1918 <span class="searchmatch">Cité</span> <span class="searchmatch">Paradis</span> Rue de <span class="searchmatch">Paradis</span> Avenue Parmentier Rue Perdonnet Cour des Petites-Écuries Passage', 'timestamp': '2018-06-09T01:45:05Z'}, {'ns': 0, 'title': 'Paradis (homonymie)', 'pageid': 1868017, 'size': 16629, 'wordcount': 1923, 'snippet': 'Wikimedia\xa0: <span class="searchmatch">paradis</span>, sur le Wiktionnaire <span class="searchmatch">Paradis</span>, sur le Wiktionnaire <span class="searchmatch">Paradis</span> est un nom de famille notamment porté par\xa0: Alysson <span class="searchmatch">Paradis</span> (1984-), actrice', 'timestamp': '2019-02-04T10:30:44Z'}, {'ns': 0, 'title': 'Vanessa Paradis', 'pageid': 74857, 'size': 87014, 'wordcount': 9333, 'snippet': 'articles homonymes, voir <span class="searchmatch">Paradis</span> (homonymie). Vanessa <span class="searchmatch">Paradis</span> Vanessa <span class="searchmatch">Paradis</span> lors du Festival de Cannes 2016. Vanessa <span class="searchmatch">Paradis</span>, née le 22 décembre 1972', 'timestamp': '2019-03-12T18:14:01Z'}, {'ns': 0, 'title': 'Les Enfants du paradis', 'pageid': 41436, 'size': 32753, 'wordcount': 3602, 'snippet': 'Pour les articles homonymes, voir Les Enfants du <span class="searchmatch">paradis</span> (homonymie). Les Enfants du <span class="searchmatch">paradis</span> Pierre Brasseur, Arletty et Jean-Louis Barrault dans un mime', 'timestamp': '2019-03-20T21:45:28Z'}, {'ns': 0, 'title': 'Paradis fiscal', 'pageid': 921525, 'size': 65559, 'wordcount': 7364, 'snippet': 'si on peut distinguer <span class="searchmatch">paradis</span> fiscal et <span class="searchmatch">paradis</span> financiers. Trois types de <span class="searchmatch">paradis</span> fiscaux peuvent être distingués\xa0: les <span class="searchmatch">paradis</span> fiscaux à faible imposition', 'timestamp': '2019-03-12T10:31:00Z'}, {'ns': 0, 'title': "Rue d'Hauteville", 'pageid': 438469, 'size': 9331, 'wordcount': 1093, 'snippet': 'd’Enghien, la rue Gabriel-Laumain, la rue des Petites-Écuries, la <span class="searchmatch">cité</span> <span class="searchmatch">Paradis</span>, la rue de <span class="searchmatch">Paradis</span>, la rue des Messageries, la rue de Chabrol. Elle mesure 773\xa0m', 'timestamp': '2019-02-27T20:42:25Z'}]}}
    result = (5653202, 'Cité Paradis')
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.get_pageid('Cité Paradis') == result

def test_getpageid2(monkeypatch):
    data = {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 737}, 'search': [{'ns': 0, 'title': 'Rue Gluck', 'pageid': 5423267, 'size': 3774, 'wordcount': 427, 'snippet': 'recommandations des projets correspondants. La <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span> est une voie du 9e\xa0arrondissement de Paris, en France. La <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span> est une voie publique située dans le', 'timestamp': '2018-03-28T13:37:29Z'}, {'ns': 0, 'title': 'Christoph Willibald Gluck', 'pageid': 182866, 'size': 24857, 'wordcount': 2855, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Gluck</span> (homonymie). Christoph Willibald <span class="searchmatch">Gluck</span> <span class="searchmatch">Gluck</span> par Joseph Siffrein Duplessis, 1775. Œuvres principales Orfeo ed Euridice', 'timestamp': '2019-03-19T11:16:42Z'}, {'ns': 0, 'title': 'Il ragazzo della via Gluck', 'pageid': 1786438, 'size': 3519, 'wordcount': 363, 'snippet': 'Miki Del Prete\xa0(it) et Luciano Beretta\xa0(it). Il est né sur la <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span> à Milan, une <span class="searchmatch">rue</span> qui donnait sur la ligne de chemin de fer, près de la gare centrale', 'timestamp': '2018-09-01T08:19:29Z'}, {'ns': 0, 'title': "L'Opéra Restaurant", 'pageid': 5649250, 'size': 4902, 'wordcount': 478, 'snippet': 'le 9e\xa0arrondissement de Paris, place Jacques-Rouché, au croisement des <span class="searchmatch">rues</span> <span class="searchmatch">Gluck</span> et Halévy. En 2007, le directeur Gerard Mortier entreprend l\'installation', 'timestamp': '2019-03-20T13:32:05Z'}, {'ns': 0, 'title': 'Rue Auber', 'pageid': 5422561, 'size': 11577, 'wordcount': 1455, 'snippet': 'une branche (la <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span>) sur la <span class="searchmatch">rue</span> Neuve-des-Mathurins, symétriquement au prolongement de la <span class="searchmatch">rue</span> de Mogador, et l\'autre branche (la <span class="searchmatch">rue</span> Halévy) vers le', 'timestamp': '2019-02-28T21:39:59Z'}, {'ns': 0, 'title': 'Un balcon à Paris', 'pageid': 8258900, 'size': 2613, 'wordcount': 225, 'snippet': 'Haussmann) de l\'appartement du 31 boulevard Haussmann, au coin de la <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span> (derrière l\'Opéra), où demeuraient Gustave Caillebotte et son frère Martial', 'timestamp': '2018-12-27T14:31:26Z'}, {'ns': 0, 'title': 'Rue Meyerbeer', 'pageid': 4309401, 'size': 3430, 'wordcount': 225, 'snippet': 'correspondants. La <span class="searchmatch">rue</span> Meyerbeer est une <span class="searchmatch">rue</span> du 9e\xa0arrondissement de Paris. Située dans le prolongement de la <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span>, elle va de la <span class="searchmatch">rue</span> Halévy à la <span class="searchmatch">rue</span> de la Chaussée-d\'Antin', 'timestamp': '2018-07-08T16:42:36Z'}, {'ns': 0, 'title': 'Gluck (homonymie)', 'pageid': 7529512, 'size': 619, 'wordcount': 75, 'snippet': 'et producteur américain Le Chevalier <span class="searchmatch">Gluck</span>, nouvelle fantastique allemande <span class="searchmatch">Rue</span> <span class="searchmatch">Gluck</span>, voie de Paris (7624) <span class="searchmatch">Gluck</span>, astéroïde Hans im <span class="searchmatch">Glück</span> (homonymie)\xa0', 'timestamp': '2018-05-14T16:40:08Z'}, {'ns': 0, 'title': 'Place Diaghilev', 'pageid': 6877421, 'size': 2085, 'wordcount': 158, 'snippet': 'la proximité du palais Garnier. L\'espace est créé lors du percement des <span class="searchmatch">rues</span> qui le bordent, vers 1865, et prend sa dénomination actuelle en 1965. Le', 'timestamp': '2018-03-27T20:00:17Z'}, {'ns': 0, 'title': "Quartier de la Chaussée-d'Antin", 'pageid': 1493993, 'size': 3419, 'wordcount': 259, 'snippet': 'Victoire, la <span class="searchmatch">rue</span> de Provence, la <span class="searchmatch">rue</span> La Fayette, la <span class="searchmatch">rue</span> Taitbout, la <span class="searchmatch">rue</span> Auber, la <span class="searchmatch">rue</span> Scribe, la <span class="searchmatch">rue</span> Halévy, la <span class="searchmatch">rue</span> <span class="searchmatch">Gluck</span>, la <span class="searchmatch">rue</span> Meyerbeer, la <span class="searchmatch">rue</span> de Chateaudun', 'timestamp': '2018-12-28T14:16:37Z'}]}}
    result = (5423267, 'Rue Gluck')
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.get_pageid('Rue Gluck') == result

def test_getstory1(monkeypatch):
    data = {'batchcomplete': '', 'warnings': {'extracts': {'*': '"exlimit" was too large for a whole article extracts request, lowered to 1.'}}, 'query': {'pages': {'5653202': {'pageid': 5653202, 'ns': 0, 'title': 'Cité Paradis', 'extract': "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."}}}}
    result ="GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.<a href='https://fr.wikipedia.org/wiki/OpenClassrooms'> [En savoir plus sur Wikipedia]</a>"
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.get_story((5653202, 'OpenClassrooms'), 'Paris') == result


def test_getstory2(monkeypatch):
    data = {'batchcomplete': '', 'warnings': {'extracts': {'*': '"exlimit" was too large for a whole article extracts request, lowered to 1.'}}, 'query': {'pages': {'5423267': {'pageid': 5423267, 'ns': 0, 'title': 'Rue Gluck', 'extract': 'La rue Gluck est une voie du 9e arrondissement de Paris, en France.\n\n\n== Situation et accès ==\nLa rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.'}}}}
    result = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.<a href='https://fr.wikipedia.org/wiki/Rue_Gluck'> [En savoir plus sur Wikipedia]</a>")
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return data

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert classes.get_story((5423267, 'Rue Gluck'), 'Paris') == result

def test_parser():
    """Test the parser function"""
    test1 = classes.parser("Salut GrandPy ! Est-ce que tu connais l'adresse \
        d'OpenClassrooms ?")
    test2 = classes.parser("salut grandpy tu peux me donner l'adresse \
        d'openclassrooms stp ?")
    assert test1 == 'OpenClassrooms' and test2 == 'openclassrooms'

def test_is_part2_number():
    """Test is_part2_number function"""
    test1 = classes.is_part2_number('OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France')
    test2 = classes.is_part2_number('Palais des sports (Parc des expositions Hall 1), Avenue Ernest Renan, St-Lambert, 15th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75015, France')
    assert test1 == True and test2 == False
