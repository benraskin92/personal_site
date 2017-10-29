from flask import Flask, render_template, request
from restaurants import get_restaurants, get_parameters
from csv_to_sql import create_connection
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    neighborhood = request.args.getlist('neighborhood') or '*'
    cost = request.args.getlist('cost') or '*'
    cuisine = request.args.getlist('cuisine') or '*'

    parameters = {"neighborhood": neighborhood, "cost": cost, "cuisine": cuisine}

    parsed_parameters = get_parameters(parameters)

    print parsed_parameters

    restaurants = get_restaurants('restaurants.csv', parsed_parameters)

    restaurants = [list(entry) for entry in restaurants]
    return render_template('homepage.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
