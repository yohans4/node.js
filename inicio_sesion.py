from flask import Flask, request

app = Flask(__name__)

@app.route("/inicio-de-sesion", methods=["POST"])
def inicio_de_sesion():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]

    # Verificamos si el usuario y la contraseña existen en la base de datos

    with open("usuarios.txt", "r") as f:
        for linea in f:
            usuario_base, contraseña_base = linea.split(":")
            if usuario == usuario_base and contraseña == contraseña_base:
                return "Autenticación satisfactoria"

    return "Error en la autenticación"