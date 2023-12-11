from flask import Flask, request

from registro import registro
from inicio_de_sesion import inicio_de_sesion

app = Flask(__name__)

@app.route("/registro", methods=["POST"])
def registro():
    return registro()


@app.route("/inicio-de-sesion", methods=["POST"])
def inicio_de_sesion():
    return inicio_de_sesion()