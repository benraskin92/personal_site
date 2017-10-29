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

def get_parameters(parameters):
    final_parameters = {}
    for k, v in parameters.iteritems():
        penultimate_list = []
        for item in v:
            if item != '*':
                penultimate_list.append('\"' + item + '\"')
        almost_there = ','.join(penultimate_list)
        final_parameters[k] = almost_there
    return final_parameters

def build_sql(parameters):
    sql = "SELECT * FROM restaurants"
    where = []

    if parameters['neighborhood']:
        where.append('neighborhood IN ({})'.format(parameters['neighborhood']))
    if parameters['cuisine']:
        where.append('cuisine IN ({})'.format(parameters['cuisine']))
    if parameters['cost']:
        where.append('cost IN ({})'.format(parameters['cost']))
    if where:
        sql = '{} WHERE {}'.format(sql, ' AND '.join(where))

    print sql
    return sql
