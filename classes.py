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


def is_part2_number(string):
    sp = string.split(',')
    count1 = 0
    for part in sp:
        if count1 != 1 and count1 != 2:
            pass
        if count1 == 1:
            temp = list(part)
            if temp[0].isdigit() == True or temp[1].isdigit() == True:
                return True
            else:
                return False
        count1 += 1


def request_map(string):
    """Give the display name and the graphical coordonates"""
    try:
        reponse = requests.get('https://eu1.locationiq.com/v1/search.php?key=b9775'\
                                'ca6dbe5cb&q=' + string + '&format=json')
        data = reponse.json()
        name = data[0]['display_name']
        lat = data[0]['lat']
        lon = data[0]['lon']
        sp = name.split(',')
        if is_part2_number(name):
            to_search = sp[2]
            city = sp[5]
        else:
            to_search = sp[1]
            city = sp[4]
        if to_search[0] == ' ':
            to_search = to_search[1:]
        if city[0] == ' ':
            city = city[1:]
        out = [name, lat, lon, to_search, city]
        return out
    except Exception as e:
        return None


def get_pageid(string):
    """Requests the MediaWiki API"""
    try:
        reponse = requests.get('https://fr.wikipedia.org/w/api.php?action=query&'\
                                'list=search&srsearch=' + string + '&utf8=&format'\
                                '=json')
        data = reponse.json()
        pageid = data['query']['search'][0]['pageid']
        title = data['query']['search'][0]['title']
        return (pageid, title)
    except:
        return None


def get_story(tup, city):
    """Return the story and the hypertext Wikipedia link"""
    if tup == None:
        return "GrandPy : Je ne me souviens d'aucune histoire sur "\
               "cet endroit !"
    else:
        try:
            pageid = tup[0]
            pagename = tup[1]
            if pagename[0] == ' ':
                pagename = pagename[1:]
            pagename = pagename.replace(' ', '_')
            reponse = requests.get('https://fr.wikipedia.org/w/api.php?action='\
                                    'query&pageids=' + str(pageid) + '&prop='\
                                    'extracts&exsentences=3%20&format=json&'\
                                    'explaintext')
            data = reponse.json()
            print(data)
            text = data['query']['pages'][str(pageid)]['extract']
            if 'Situation et accès ==\n' in text:
                text = text.split('Situation et accès ==\n')
                story = text[1]
            else:
                text = text.split('.')
                story = text[0] + text[1]
            if '==' in story:
                story = story.split('==')[0]
            pagename = pagename.replace("'", "%27")
            beginning = "GrandPy : Mais t'ai-je déjà raconté l'histoire de cet "\
                        "endroit qui m'a vu en culottes courtes ? "
            more =  "<a href='https://fr.wikipedia.org/wiki/" + pagename + \
                    "'> [En savoir plus sur Wikipedia]</a>"
            rep = beginning + story + more
            return rep
        except:
            pass