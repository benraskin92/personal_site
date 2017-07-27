from flask import Flask, render_template, request
from restaurants import get_restaurants
from csv_to_sql import create_connection
import csv

app = Flask(__name__)

@app.route('/')
def index():
    neighborhood = request.args.get('neighborhood') or '*'
    cost = request.args.get('cost') or '*'
    cuisine = request.args.get('cuisine') or '*'

    print "neighborhood {}".format(neighborhood)

    parameters = {"neighborhood": neighborhood, "cost": cost, "cuisine": cuisine}

    print parameters

    restaurants = get_restaurants('restaurants.csv', parameters)

    restaurants = [list(entry) for entry in restaurants]
    return render_template('homepage.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
