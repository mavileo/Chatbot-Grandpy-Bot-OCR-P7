# Create GrandPy Bot, the granddaddy-robot  🤖 👴

Chatbot giving information about places

## Local launching
Git clone the repo.\
Create a python3 virtualenv and install the requirements.\
Launch __init__.py file.\
Go to the url that flask gives you.

```bash
git clone https://github.com/m-a-xX/Project_7-OpenClassrooms.git
cd Project_7-OpenClassrooms
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements
```

## Go to the web app

Go to the following link : https://grandpychatbot.herokuapp.com/


## How to use

You can ask a question in french to the chatbot about a place like "Tu sais où est le musée du Louvre ?", he will answer you with a map of the place you searched and the story of the place.


## How it works

When you ask the chatbot a question, it will query the OpenStreetMap Rest API to retrieve the exact name of the place as well as these coordinates, with that we get the map of this place thanks to Mapbox, then we query the API from Wikipedia to retrieve the summary of this place. The requests are made in Javascript using jQuery.
