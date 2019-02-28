from flask import Flask, request
import json
import classes
app = Flask(__name__)


@app.route('/')
def chat():
    with open("/home/intmax/Documents/OpenClassrooms/Projet7/Projet/templates/"\
              "index.html", 'r') as file:  
        data = file.read()
    return data

@app.route('/map')
def map():
    inp = request.args.get('value') 
    rep1 = classes.request_map(classes.parser(inp))
    rep3 = rep1[3]
    if rep3[0] == ' ':
        rep3 = rep3[1:]
    rep3 = rep3.replace(' ', '_')
    rep2 = classes.get_story(classes.get_pageid(rep1[3]), rep3)
    result = (rep1, rep2, rep3)
    return json.dumps(result)

if __name__== "__main__":
    app.run()
