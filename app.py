from flask import Flask, jsonify, request  
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GET -> Consultar

@app.route("/productos", methods=["GET"])  
def ver_productos():
    db = mysql.connector.connect(  
        host="localhost",
        user="root",  
        password="12345",  
        database="comercio"  
    )
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")  
    
    productos = cursor.fetchall()
    
    cursor.close()
    db.close()  
    return jsonify(productos)

# DELETE -> Eliminar un elemento
@app.route("/eliminar_producto/<int:id>", methods=["DELETE"])  
def eliminar_producto(id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="12345",  
        database="comercio"  
    )
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    db.close()  
    return jsonify({"mensaje": "ELIMINADO!"})

# POST -> Nuevo elemento en el servidor
@app.route("/nuevo_producto", methods=["POST"])  
def agregar_productos():
    info = request.json  
    db = mysql.connector.connect(  
        host="localhost",
        user="root",  
        password="12345",  
        database="comercio" 
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)", (info["nombre"], info["cantidad"], info["precio"]))  # Fixed syntax
    db.commit()
    cursor.close()
    db.close()  
    return jsonify({"mensaje": "AGREGADO CON EXITO"})

# PUT -> Actualizar completamente un elemento
@app.route("/actualizar_producto/<int:id>", methods=["PUT"])  
def modificar_producto(id):
    info = request.json  
    db = mysql.connector.connect(  
        host="localhost",
        user="root",  
        password="12345",  
        database="comercio"  
    )
    cursor = db.cursor()
    cursor.execute("UPDATE productos SET nombre=%s, cantidad=%s, precio=%s WHERE id=%s", (info["nombre"], info["cantidad"], info["precio"], id))  # Fixed syntax and order
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"mensaje": "ACTUALIZADO CON EXITO"})

if __name__ == "__main__":
    app.run(debug=True)
