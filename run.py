from flask import Flask, render_template, request #RenderTemplate #request: petición
import csv

app = Flask(__name__) #Creamos nuestra aplicación

@app.route("/")
def index():
    fventas = open ("./sales.csv", "r") #enrutamos la librería.
    csvreader = csv.reader(fventas, delimiter=",") #leemos y delimitamos hasta la coma

    registros = []
    d = {}
    for linea in csvreader:
        registros.append(linea)
        if linea[0] in d:
            d[linea[0]]["ingresos"]+= round(float(linea[11]),2)
            d[linea[0]]["beneficios"] += round(float(linea[13]),2)

        else:
            if linea[0] != "region":
                d[linea[0]] = {"ingresos": round(float(linea[11]),2), "beneficios": round(float(linea[13]),2)}
   

    return render_template("region.html", ventas=d)




   