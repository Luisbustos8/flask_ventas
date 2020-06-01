import sqlite3
import csv

filename = "./sales10.csv"
database = "./data/ventas.db"

conn = sqlite3.connect(database) 
cur = conn.cursor()

fsales = open(filename, "r")
csvreader = csv.reader(fsales, delimiter=",")

headerRow = next(csvreader)
print(headerRow)

query = "INSERT OR IGNORE into productos (tipo_producto, precio_unitario, coste_unitario) values (?, ?, ?);"
for dataRow in csvreader:
    tupla_datos = ( dataRow[2], float(dataRow[9]), float(dataRow[10]))
    cur.execute(query, tupla_datos)
  
conn.commit() #Confirmamos cambios.
conn.close() #Cerramos base de datos.