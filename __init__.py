from flask import Flask, request
import json
import classes
app = Flask(__name__)


@app.route('/')
def chat():
    with open("templates/index.html", 'r') as file:  
        data = file.read()
    return data

@app.route('/map')
def map():
    inp = request.args.get('value') 
    loc = classes.request_map(classes.parser(inp))
    if loc == None:
        return 'GrandPy : Je ne vois pas de quel endroit tu parles'
    else:
        rep_wiki = classes.story(classes.get_pageid(loc[3]), loc[4])
        result = (loc, rep_wiki)
        return json.dumps(result)
