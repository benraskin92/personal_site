import sqlite3
from csv_to_sql import create_connection


def get_restaurants(db, parameters):
    conn, cur = create_connection('restaurants.db')

    print str(parameters['neighborhood'])
    print str(parameters['cuisine'])
    print str(parameters['cost'])

    cur.execute(build_sql(parameters))
    restaurants = cur.fetchall()

    print "restaurants!!! {}".format(restaurants)

    return restaurants

def build_sql(parameters):
    sql = "SELECT * FROM restaurants"
    where = []
    if parameters['neighborhood'] != '*':
        where.append('neighborhood = \"{}\"'.format(parameters['neighborhood']))
    if parameters['cuisine'] != '*':
        where.append('cuisine = {}'.format(parameters['cuisine']))
    if parameters['cost'] != '*':
        where.append('cost = {}'.format(parameters['cost']))
    if where:
        sql = '{} WHERE {}'.format(sql, ' AND '.join(where))
    print sql
    return sql
