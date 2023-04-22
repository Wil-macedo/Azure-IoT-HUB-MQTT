from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap 
from Server_IoT.hub_Tot import *

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return redirect(url_for("predio"))

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/predio")
def predio():
    return render_template('predio.html')


@app.route("/mqtt/<andar>/<ligar>")
def mqtt(andar, ligar):
    result = None
    while result is None:
        try:
            result = iothub_devicemethod_sample_run(andar, ligar)
        except Exception as ex:
            print(ex)
    return redirect(url_for("predio"))

app.run(host='0.0.0.0', debug=True)


