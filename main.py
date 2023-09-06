import os
import mysql.connector 
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "mytoken"


def recipes():
    mydb = mysql.connector.connect(
        host="containers-us-west-53.railway.app",
        user="root",
        password="ZnKm3FY3rnSv1642dwtH",
        database="railway",
        port=7314
    )
    mycursor = mydb.cursor()
    sql = "select * from recipes where id = 1"
    mycursor.execute(sql)
    mydb.commit()
    return True

# Datos de ejemplo de recetas
recetas = [sql]

# Ruta para obtener una receta aleatoriaz
@app.route('/receta_aleatoria', methods=['GET'])
def obtener_receta_aleatoria():
    receta_aleatoria = random.choice(recetas)
    return jsonify({'receta': receta_aleatoria})

if _name_ == '_main_':
    app.run(debug=True)



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

"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 