from flask import Flask
import csv

app = Flask(__name__) #Creamos nuestra aplicación

@app.route("/")
def index():
    fventas = open ("./sales10.csv", "r")
    csvreader = csv.reader(fventas, delimiter=",")

    registros = []
    d = {}
    for linea in csvreader:
        registros.append(linea)
        if linea[0] in d:
            d[linea[0]]["ingresos"] += float(linea[11])
            d[linea[0]]["beneficios"] += float(linea[13])

        else:
            if linea[0] != "region":
                d[linea[0]] = {"ingresos": float(linea[11]), "beneficios": float(linea[13])}
   

    return d
