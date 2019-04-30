import os
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')


def test_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("insert into measure(id,termometer_id,temperature) values (DEFAULT,2,23.000000)")

    cur.close()
    conn.close()


if __name__ == '__main__':
    test_db()
