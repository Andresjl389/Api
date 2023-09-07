import os
import mysql.connector 
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "mytoken"


def recipes(Ingredientes_principal = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-53.railway.app",
        user="root",
        password="ZnKm3FY3rnSv1642dwtH",
        database="railway",
        port=7314
    )
    mycursor = mydb.cursor()
    sql = "select * from recipes where Ingrediente_principal = '"+Ingredientes_principal+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

recetas = recipes()

# Ruta para obtener una receta aleatoriaz
@app.route('/receta_aleatoria', methods=['GET'])
def obtener_receta_aleatoria():
    receta_aleatoria = recipes()
    print(receta_aleatoria)
    return jsonify({'receta': receta_aleatoria})

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
    mydb2 = mysql.connector.connect(
        host="containers-us-west-53.railway.app",
        user="root",
        password="ZnKm3FY3rnSv1642dwtH",
        database="railway",
        port=7314
    )

    Id = request.form['id']
    NomReceta = request.form['Nombre_receta']
    Description = request.form['Descripcion']
    Ingredients = request.form['Ingredientes']
    Ingre_Principal = request.form['Ingrediente_principal']


   


    mycursor = mydb2.cursor()
    mycursor.execute("INSERT INTO recipes (id, Nombre_receta, Descripcion, Ingredientes, Ingrediente_principal) values (%s, %s, %s, %s, %s)", (Id, NomReceta, Description, Ingredients, Ingre_Principal))   

    mydb2.commit()
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


"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    # app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000))
