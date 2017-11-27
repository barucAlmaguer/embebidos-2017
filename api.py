from flask import jsonify
from flask import Markup
from flask import Flask
from flask import render_template

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

def get_sensordata():
    cur = conn.cursor()
    cur.execute("SELECT dato from RANDOM ORDER BY id desc;")
    dic = {}
    for i, dato in enumerate(cur):
        dic[i] = dato
    return dic

@app.route('/mundocruel/')
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
    cur.execute("SELECT dato from RANDOM ORDER BY id desc;")
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

@app.route("/")
def chart():
    #labels = ["January","February","March","April","May","June","July","August"]
    #values = [10,9,8,7,6,4,7,8]
    d = get_sensordata()
    labels = [d for d in list(d.keys())]
    values = [d[0] for d in list(d.values())]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)