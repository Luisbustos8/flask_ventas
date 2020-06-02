import csv, sqlite3

from the_app import app
from the_app.forms import ProdutForm


from flask import render_template, request, redirect, url_for

BASE_DATOS = "./data/ventas.db"

@app.route("/")
def index():
    fventas = open ("./sales10.csv", "r") #enrutamos la librería.
    csvreader = csv.reader(fventas, delimiter=",") #leemos y delimitamos hasta la coma

   
    d = {}
    for linea in csvreader:
        if linea[0] in d:
            d[linea[0]]["ingresos"]+= float(linea[11])
            d[linea[0]]["beneficios"] += float(linea[13])

        else:
            if linea[0] != "region":
                d[linea[0]] = {"ingresos": float(linea[11]), "beneficios": float(linea[13])}
   

    return render_template("region.html", ventas=d)

@app.route("/paises")
def paises():
    region_name = request.values["region"] #OBJETO PETICION REQUEST, COGEMOS VALOR VALUES

    fventas = open("./sales10.csv", "r")
    csvreader= csv.reader(fventas, delimiter=",")#Creas variable de fventas y lo delimitas por una coma.

    d = {}
    for linea in csvreader:
        if linea[0] == region_name: #Es pais igual al pais que deseamos
            if linea [1] in d: #si está region en diccionario
                d[linea[1]]["ingresos"]+= float(linea[11]) #obtener y añadir valor ingresos
                d[linea[1]]["beneficios"] += float(linea[13]) #obtener y añadir valor beneficios
            else: #si no está en el diccionario me lo creas y guardas región, ingresos y beneficios
                d[linea[1]] = {"ingresos": float(linea[11]), "beneficios": float(linea[13])}
   


    return render_template('pais.html', ventas_pais=d, region_nm=request.values['region'])

@app.route("/productos")
def productos(): #Funcion url_form. Lo traemos aquí para que haga este proceso.
    conn = sqlite3.connect(BASE_DATOS)
    cur = conn.cursor()

    query = "SELECT id, tipo_producto, precio_unitario, coste_unitario FROM productos;"
    productos = cur.execute(query).fetchall()

    conn.close()
    return render_template("productos.html", productos=productos)

@app.route("/addproducto", methods=["GET", "POST"])
def addproduct():
    form = ProdutForm()

    if request.method == "GET":
        return render_template("newproduct.html", form=form)
    else:
        conn = sqlite3.connect(BASE_DATOS)
        cur = conn.cursor()
        query = "INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) values (?,?,?);"
        datos= (request.values.get("tipo_producto"), request.values.get("precio_unitario"), request.values.get("coste_unitario"))
        
        cur.execute (query, datos) 
        conn.commit()
        conn.close()
        

        return redirect(url_for("productos")) #ponemos el nombre de la función

