"""This file contains tests"""

import requests
import classes
"""This file contains tests"""

import requests
import classes

import urllib.request

from io import BytesIO
import json

def test_http_return1(monkeypatch):
    results = ['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885', 'Cité Paradis', 'Paris']

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.request_map('OpenClassrooms') == results

def test_http_return2(monkeypatch):
    results = ['Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.86616135', '2.31222295966943', 'Avenue du Général Eisenhower', 'Paris']

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.request_map('grand palais') == results

def test_http_return3(monkeypatch):
    results = (5653202, 'Cité Paradis')

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.get_pageid('Cité Paradis') == results

def test_http_return4(monkeypatch):
    results = (5423267, 'Rue Gluck')

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.get_pageid('Rue Gluck') == results

def test_http_return5(monkeypatch):
    results = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.<a href='https://fr.wikipedia.org/wiki/OpenClassrooms'> [En savoir plus sur Wikipedia]</a>")

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.get_story((5653202, 'OpenClassrooms'), 'Paris') == results

def test_http_return6(monkeypatch):
    results = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.<a href='https://fr.wikipedia.org/wiki/Rue_Gluck'> [En savoir plus sur Wikipedia]</a>")

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert classes.get_story((5423267, 'Rue Gluck'), 'Paris') == results

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

def test_request_map():
    """Test request_map function"""
    test1 = classes.request_map('OpenClassrooms')
    test2 = classes.request_map('grand palais')
    rep1 = (['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885', 'Cité Paradis', 'Paris'])
    rep2 = (['Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.86616135', '2.31222295966943', 'Avenue du Général Eisenhower', 'Paris'])
    assert test1 == rep1 and test2 == rep2

def test_get_pageid():
    """Test get_page fucntion"""
    test1 = classes.get_pageid('Cité Paradis')
    test2 = classes.get_pageid('Rue Gluck')
    rep1 = (5653202, 'Cité Paradis')
    rep2 = (5423267, 'Rue Gluck')
    assert test1 == rep1 and test2 == rep2

def test_get_story():
    """Test get_story function"""
    test1 = classes.get_story((5653202, 'OpenClassrooms'), 'Paris')
    test2 = classes.get_story((5423267, 'Rue Gluck'), 'Paris')
    rep1 = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.<a href='https://fr.wikipedia.org/wiki/OpenClassrooms'> [En savoir plus sur Wikipedia]</a>")
    rep2 = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.<a href='https://fr.wikipedia.org/wiki/Rue_Gluck'> [En savoir plus sur Wikipedia]</a>")
    assert test1 == rep1 and test2 == rep2
