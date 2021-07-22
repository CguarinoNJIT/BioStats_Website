from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response


app = Flask(__name__)


def biostats_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'database': 'bioData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM biostats')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index() -> str:
    user = {'username': 'Chris'}
    biostatsData = biostats_import()
    return render_template('index.html', title='Bio Stats', user=user, biostats=biostatsData)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')