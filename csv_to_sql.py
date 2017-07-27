import csv, sqlite3

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur
