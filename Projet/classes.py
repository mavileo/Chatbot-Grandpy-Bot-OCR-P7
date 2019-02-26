"""This file contains python classes used by the web app"""

import json, requests
import stop_words

def parser(string):
    """Parse the string enter in argument"""
    string = string.replace("l'", "")
    string = string.replace("d'", "")
    string = string.replace("m'", "")
    string = string.replace("t'", "")
    sp = string.split()
    f_list = []
    for word in sp:
        if word not in stop_words.stop_words:
            f_list.append(word)
            f_str = ' '.join(f_list)
    return f_str

def request(string):
    """Give the display name and the graphical coordonates"""
    reponse = requests.get('https://eu1.locationiq.com/v1/search.php?key=b9775ca6dbe5cb&q=' + string + '&format=json')
    data = reponse.json()
    count = 0
    for result in data:
        if count == 0:
            name = result['display_name']
            lat = result['lat']
            lon = result['lon']
    out = [name, lat, lon]
    return out

print(parser("Bonjour GrandPy ! Est-ce que tu peux m'indiquer l'adresse d'OpenCLassRooms s'il te plaît ?"))