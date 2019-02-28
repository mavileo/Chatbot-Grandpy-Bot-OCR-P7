"""This file contains tests"""

import classes
import requests

def test_parser():
    """Test the parser function"""
    test1 = classes.parser("Salut GrandPy ! Est-ce que tu connais l'adresse \
        d'OpenClassrooms ?")
    test2 = classes.parser("salut grandpy tu peux me donner l'adresse \
        d'openclassrooms stp ?")
    assert test1 == 'OpenClassrooms' and test2 == 'openclassrooms'

def test_request_map():
    """Test request_map function"""
    test1 = classes.request_map('OpenClassrooms')
    test2 = classes.request_map('grand palais')
    rep1 = (['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885', ' Cité Paradis'])
    rep2 = (['Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.86616135', '2.31222295966943', ' Avenue du Général Eisenhower'])
    assert test1 == rep1 and test2 == rep2

def test_get_pageid():
    """Test get_page fucntion"""
    test1 = classes.get_pageid('Cité Paradis')
    test2 = classes.get_pageid('Rue Gluck')
    rep1 = 5653202
    rep2 = 5423267
    assert test1 == rep1 and test2 == rep2

def test_get_story():
    """Test get_story function"""
    test1 = classes.get_story(5653202)
    test2 = classes.get_story(5423267)
    rep2 = ("La rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.")
    rep1 = ("La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.")
    assert test1 == rep1
