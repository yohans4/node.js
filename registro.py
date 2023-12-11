from flask import Flask, request

app = Flask(__name__)

@app.route("/registro", methods=["POST"])
def registro():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]

    # Almacenamos el usuario y la contraseña en la base de datos

    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario}:{contraseña}\n")

    return "Registro satisfactorio"