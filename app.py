import os
import psycopg2
from flask import Flask, render_template, g

my_app = Flask(__name__)

def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

@my_app.before_request
def before_request():
    g.db_conn = connect_db()

@my_app.route('/')
def index():
    cur = g.db_conn.cursor()
    cur.execute("SELECT * FROM termometer;")
    return render_template('index.html', termometers=cur.fetchall())


if __name__ == '__main__':
    my_app.run()
