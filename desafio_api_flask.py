"""
    This code it's a challenge propourse by DIO.
    This challenge it's to create a API using the framework Flask.
"""
import random as rk
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify

app = Flask(__name__) #the name of the application package
run_with_ngrok(app)

planilha = [{
    'number': '1',
    'name': 'Mahesh',
    'age': '25',
    'city': 'Bangalore',
    'country': 'India'
},
{
    'number': '2',
    'name': 'Alex',
    'age': '26',
    'city': 'London',
    'country': 'UK'
},
{
    'number': '3',
    'name': 'David',
    'age': '27',
    'city': 'San Francisco',
    'country': 'USA'
},
{
    'number': '4',
    'name': 'John',
    'age': '28',
    'city': 'Toronto',
    'country': 'Canada'
},
{
    'number': '5',
    'name': 'Chris',
    'age': '29',
    'city': 'Paris',
    'country': 'France'
}]

result = []

for person in planilha:
    result.append(person)

print(result)

@app.route("/input") #code to assign Input URL in our app to function input.

def url_input():
    """
        On this function we set what will have on the URL /input
    """
    return jsonify(result) # "d" is the dictionary we defined

@app.route('/output', methods=['GET','POST']) #output page

def pred_json():
    """
        On this function we set what will have on the URL /output
    """
    pred = rk.choice(["positive","negative"])
    nd = rk.choice(result) # our input
    nd["prediction"]=pred
    return jsonify(nd)

app.run()
