import sqlite3, csv

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur

def create_table():

    conn, cur = create_connection('restaurants.db')
    cur.execute("DROP TABLE IF EXISTS restaurants")
    cur.execute("CREATE TABLE restaurants (neighborhood, cuisine, name, cost, complete, notes, line, menu, favorite_items, address);")

    with open('restaurants.csv', 'rb') as rest_file:
        data = csv.DictReader(rest_file)
        to_db = [(i['neighborhood'], i['cuisine'], i['name'], i['cost'], i['complete'], i['notes'], i['line'], i['menu'], i['favorite_items'], i['address']) for i in data]

    cur.executemany("INSERT INTO restaurants (neighborhood, cuisine, name, cost, complete, notes, line, menu, favorite_items, address) VALUES (?,?,?,?,?,?,?,?,?,?);", to_db)
    conn.commit()
    conn.close()

create_table()