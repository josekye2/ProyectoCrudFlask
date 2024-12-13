from flask import  Flask, render_template, jsonify, request
 
carros=[
    {
        "id":"1",
        "marca":"mazda",
        "modelo":1983
    },{
        "id":"2",
        "marca":"honda",
        "modelo":1993
    }
]

usuarios=[
    {
        "id":"1",
        "nombre":"Juan",
        "email":"juansanto@gmail.com"
    },{
        "id":"2",
        "nombre":"Camila",
        "email":"camilitap@gmail.com"
    }
]

app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(carros)
 
@app.route("/carros", methods=["POST"])
def post_carros():
    nuevoCarro = request.json
    carros.append(nuevoCarro)
    return "nuevo carro creado", 201

@app.route("/carros/<id>", methods=["DELETE"])
def delete_carro (id):
    global carros
    carros = [carro for carro in carros if carro["id"] != id]
    return f"Carro con id {id} ha sido eliminado", 200
 
@app.route("/carros/<id>", methods=["PUT"])
def put_carro (id):
    nuevocarro = request.json
    for index, carro in enumerate(carros):
        if carro["id"] == id:
            carro = carros.index(carro)
            carros[index] = nuevocarro
            return "carro actualizado", 202
    return "carro no econtrado", 404

# Rutas para el CRUD de usuarios

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)
 
@app.route("/usuarios", methods=["POST"])
def post_usuario():
    nuevo_usuario = request.json
    carros.append(nuevo_usuario)
    return "nuevo usuario creado", 201

@app.route("/usuario/<id>", methods=["DELETE"])
def delete_usuario (id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    return f"Usuario con id {id} ha sido eliminado", 200
 
@app.route("/usuarios/<id>", methods=["PUT"])
def put_usuario(id):
    nuevo_usuario = request.json
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuario = usuarios.index(usuario)
            usuarios[index] = nuevo_usuario
            return "Usuario actualizado", 202
    return "Usuario no econtrado", 404
 
app.run()


