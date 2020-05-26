from flask import Flask


app = Flask(__name__) #Creamos nuestra aplicación

@app.route("/")
def index():
    return "Hola, mundo"