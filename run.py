from flask import Flask, render_template, request #RenderTemplate #request: petición
import csv

app = Flask(__name__) #Creamos nuestra aplicación

@app.route("/")
def index():
    fventas = open ("./sales.csv", "r") #enrutamos la librería.
    csvreader = csv.reader(fventas, delimiter=",") #leemos y delimitamos hasta la coma

   
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

@app.route("/paises")
def paises():
    region_name = request.values["region"]

    fventas = open("./sales.csv", "r")
    csvreader= csv.reader(fventas, delimiter=",")

    d = {}
    for linea in csvreader:
        if linea[0] == region_name: #Es pais igual al pais que deseamos
            if linea [1] in d: #si está region en diccionario
                d[linea[1]]["ingresos"]+= round(float(linea[11]),2) #obtener y añadir valor ingresos
                d[linea[1]]["beneficios"] += round(float(linea[13]),2) #obtener y añadir valor beneficios
            else: #si no está en el diccionario me lo creas y guardas región, ingresos y beneficios
                d[linea[1]] = {"ingresos": round(float(linea[11]),2), "beneficios": round(float(linea[13]),2)}
   


    return render_template("paises.html", ventas=d)




   