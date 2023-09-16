import os
import mysql.connector 
from functools import wraps
from flask import Flask, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = "mytoken"

try:
    client = MongoClient("mongodb+srv://Andreses:qO0eRncJlMS4f78t@cluster0.eydrwxt.mongodb.net/")
    db = client["Generador_Recetas"]
    collection = db["recetas"]
    client.server_info()
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar la base de datos: ", str(e))

# db = client["Generador_Recetas"]
# collection = db["recetas"]
# client.server_info()
# print("conexion exitosa")



def recipes(Ingredientes_principal = ""):
    
    # db = mysql.connector.connect(
    #     host="andresarevalo.mysql.pythonanywhere-services.com",
    #     user="andresarevalo",
    #     password="febrero23",
    #     database="andresarevalo$Products"
    # ) 
    
    # cursor = db.cursor()
    # sql = "select * from recipes where Ingrediente_principal = '"+Ingredientes_principal+"'"
    # cursor.execute(sql)
    # myresult = mycursor.fetchall()
    return myresult


# Ruta para obtener una receta aleatoriaz
@app.route('/receta_aleatoria', methods=['GET'])
def obtener_receta_aleatoria():
    resultado = collection.find({"ingrediente_principal": "dcsdds"})
    
    # receta_aleatoria = recipes()
    # print(receta_aleatoria)
    
    print(busqueda)
    return jsonify({'receta seleccionada': busqueda})

if __name__ == '_main_':
    app.run(debug=True)


@app.route('/nom_receta', methods=['POST'])

def receta_Post():
        nombre_receta = request.form['ingrediente_receta']
        # ingrediente_principal = request.args
        # s_ingrediente = args.get("ingrediente_receta")
        
        # print(s_ingrediente)
        
        respuesta = recipes(nombre_receta)
        
        print("================================================")
        print("El ingrediente principal de la receta es "+nombre_receta)
        print("================================================")
        
        return jsonify({'receta': respuesta})


@app.route('/create_receipe', methods=['POST'])

def create_Post():
    
    # db = mysql.connector.connect(
    #     host="AndresJaimes389.mysql.pythonanywhere-services.com",
    #     user="AndresJaimes389",
    #     password="Gerecetas",
    #     database="AndresJaimes389$Proyect"
    # ) 
    
    # cursor = db.cursor()

    Id = request.form['id']
    NomReceta = request.form['Nombre_receta']
    Description = request.form['Descripcion']
    Ingredients = request.form['Ingredientes']
    Ingre_Principal = request.form['Ingrediente_principal']


    
    # cursor.execute("INSERT INTO Recipes (id, nombre, descripcion, ingredientes, ingrediente_principal) values (%s, %s, %s, %s, %s)", (Id, NomReceta, Description, Ingredients, Ingre_Principal))   
    # db.commit()
    # cursor.close()
    return jsonify({"Id ": Id, "Nombre receta": NomReceta, "Descripcion ": Description, "Ingredientes ": Ingredients, "Ingrediente principal ": Ingre_Principal})
    


def token_required(f):
     @wraps(f)
     def validate(*args, **kwargs):
         client_token = request.headers['mytoken']
         server_token = app.config['SECRET_KEY']
         #server_token = "securetoken"
         if client_token == server_token:
             return f(*args, **kwargs)
         else:
             return jsonify({"message":"token is invalid"}), 403    
     return validate 

{
  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
}


# """
# MAIN ...........................................................................
# """
# if __name__ == '__main__':
#     # app.run()
#     app.run(debug=True, port=os.getenv("PORT", default=5000))
