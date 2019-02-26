from flask import Flask, request
import json
import classes
app = Flask(__name__)


@app.route('/')
def chat():
    with open("/home/intmax/Documents/OpenClassrooms/Projet7/Projet/templates/index.html", 'r') as file:  
        data = file.read()
    return data

@app.route('/test')
def test():
    inp = request.args.get('value') 
    result = classes.request(classes.parser(inp))
    return json.dumps(result)

if __name__== "__main__":
    app.run()
