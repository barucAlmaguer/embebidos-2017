from flask import Flask, jsonify

import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

app = Flask(__name__)

@app.route('/')
def mainpage():
    return "hola mundo cruel"

#'/post/<int:post_id>'
@app.route('/log/<int:value>')
def logging(value):
    cur = conn.cursor()
    cur.execute("INSERT into RANDOM (dato) values ({});".format(value))
    conn.commit()
    return "dato posteado: {}".format(value)

@app.route('/view/<int:value>')
def view_table(value):
    response = ""
    cur = conn.cursor()
    cur.execute("SELECT dato from RANDOM ORDER BY id desc;");
    for i, dato in enumerate(cur):
        if i >= value:
            break
        response += "{}={}<br>".format(i, dato[0])
    return response


@app.route('/json/<int:value>')
def view_json(value):
    response = view_table(value)
    response_list = response.strip("<br>").split("<br>")
    d = {}
    for res in response_list:
        k, v = res.split('=')
        d[k] = v
    return jsonify(d)
