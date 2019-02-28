"""This file contains python classes used by the web app"""

import json, requests
import stop_words

lat=''
lon=''

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

def request_map(string):
    """Give the display name and the graphical coordonates"""
    reponse = requests.get('https://eu1.locationiq.com/v1/search.php?key=b9775'\
                            'ca6dbe5cb&q=' + string + '&format=json')
    data = reponse.json()
    name = data[0]['display_name']
    lat = data[0]['lat']
    lon = data[0]['lon']
    story = ''
    sp = name.split(',')
    count1 = 0
    for part in sp:
        if count1 != 1 and count1 != 2:
            pass
        if count1 == 1:
            temp = list(part)
            if temp[0].isdigit() == True or temp[1].isdigit() == True:
                story = sp[2]
            else:
                story = part
        count1 += 1
    out = [name, lat, lon, story]
    return out


def get_pageid(string):
    """Requests the MediaWiki API"""
    reponse = requests.get('https://fr.wikipedia.org/w/api.php?action=query&'\
                            'list=search&srsearch=' + string + '&utf8=&format'\
                            '=json')
    data = reponse.json()
    return data['query']['search'][0]['pageid']

def get_story(pageid, pagename):
    try:
        reponse = requests.get('https://fr.wikipedia.org/w/api.php?action='\
                                'query&pageids=' + str(pageid) + '&prop='\
                                'extracts&exsentences=3%20&format=json&'\
                                'explaintext')
        data = reponse.json()
        text = data['query']['pages'][str(pageid)]['extract']
        text = text.split('Situation et accès ==\n')
        story = text[1]
        beginning = "GrandPy : Mais t'ai-je déjà raconté l'histoire de cet "\
                    "endroit qui m'a vu en culottes courtes ? "
        more =  "<a href='https://fr.wikipedia.org/wiki/" + pagename + \
                "'> [En savoir plus sur Wikipedia]</a>"
        rep = beginning + story + more
    except Exception as e:
        rep = "GrandPy : Je ne me souviens d'aucune histoire sur cet endroit !"
    return rep
