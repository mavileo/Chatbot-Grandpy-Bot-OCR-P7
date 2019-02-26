"""This file contains tests"""

import classes
import requests

def test_parser():
    test1 = classes.parser("Salut GrandPy ! Est-ce que tu connais l'adresse \
        d'OpenClassrooms ?")
    test2 = classes.parser("salut grandpy tu peux me donner l'adresse \
        d'openclassrooms stp ?")
    assert test1 == 'OpenClassrooms' and test2 == 'openclassrooms'

def test_request():
    test1 = classes.request('OpenClassrooms')
    test2 = classes.request('grand palais paris')
    rep1 = (['OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10th Arrondissement, Paris, Ile-de-France, Metropolitan France, 75010, France', '48.8747786', '2.3504885'])
    rep2 = (['Grand Palais, Avenue Gabriel, Madeleine, 8th Arrondissement of Paris, Paris, Ile-de-France, Metropolitan France, 75008, France', '48.8683694', '2.3166122'])
    assert test1 == rep1 and test2 == rep2
