import os
import psycopg2
from psycopg2 import sql
from flask import Flask, render_template, g, request, Response, redirect, url_for

my_app = Flask(__name__)




def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))


@my_app.before_request
def before_request():
    g.db_conn = connect_db()
    g.db_conn.autocommit = True


@my_app.route('/handle_measure', methods=['POST'])
def handle_measure():
    temp = float(request.form['measure_value'])
    termo_id = int(request.form['termometer_id'])
    strt = "insert into measure(id,termometer_id,temperature) values (DEFAULT,%d,%f)" % (termo_id, temp)
    print(strt)
    curs = g.db_conn.cursor()
    curs.execute(sql.SQL(strt))
    return redirect(url_for('index'))
    # your code
    # return a response


@my_app.route('/')
def index():
    cur = g.db_conn.cursor()
    cur.execute("SELECT * FROM termometer;")

    #
    cur_1 = g.db_conn.cursor()
    cur_1.execute("SELECT * FROM measure;")
    return render_template('index.html', termometers=cur.fetchall(), measures=cur_1.fetchall())


if __name__ == '__main__':
    my_app.run()
