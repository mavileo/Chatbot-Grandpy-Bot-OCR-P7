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

def test_is_part2_number():
    """Test is_part2_number function"""
    test1 = classes.is_part2_number('OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France')
    test2 = classes.is_part2_number('Palais des sports (Parc des expositions Hall 1), Avenue Ernest Renan, St-Lambert, 15th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75015, France')
    assert test1 == True and test2 == False

def test_request_map():
    """Test request_map function"""
    test1 = classes.request_map('OpenClassrooms')
    test2 = classes.request_map('grand palais')
    rep1 = (['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885', 'Cité Paradis'])
    rep2 = (['Grand Palais, Avenue du Général Eisenhower, Champs-Élysées, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.86616135', '2.31222295966943', 'Avenue du Général Eisenhower'])
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
    test1 = classes.get_story(5653202, 'OpenClassrooms')
    test2 = classes.get_story(5423267, 'Rue Gluck')
    rep1 = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.<a href='https://fr.wikipedia.org/wiki/OpenClassrooms'> [En savoir plus sur Wikipedia]</a>")
    rep2 = ("GrandPy : Mais t'ai-je déjà raconté l'histoire de cet endroit qui m'a vu en culottes courtes ? La rue Gluck est une voie publique située dans le 9e arrondissement de Paris. Elle débute  place Jacques-Rouché et se termine place Diaghilev.<a href='https://fr.wikipedia.org/wiki/Rue Gluck'> [En savoir plus sur Wikipedia]</a>")
    assert test1 == rep1
