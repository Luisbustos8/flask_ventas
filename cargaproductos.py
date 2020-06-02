import csv, sqlite3 #IMPORTAR LAS LIBRERÍAS

filename = "./sales10.csv" #Nombre del fichero en una variable.
database = "./data/ventas.db" #Fichero de database tambien dentro de una variable.

conn = sqlite3.connect(database) #Crear conexion de base de datos. 
cur = conn.cursor() #elemento de pyhton para base de datos.

fSales = open(filename, 'r') #ruta y abrimos en modo de lectura.
csvreader = csv.reader(fSales, delimiter=",") #Creamos un reader y ponemos el delimitador.

headerRow = next(csvreader) #Creamos variable con la función next, para ir fila por fila.
print(headerRow)

query = 'INSERT OR IGNORE INTO productos (tipo_producto, precio_unitario, coste_unitario) values (?, ?, ?);' # Query que quiero realizar
for dataRow in csvreader: #Esto para las siguientes filas.
    tupla_datos = ( dataRow[2], float(dataRow[9]), float(dataRow[10]) ) #Creamos la tupla (?,?,?). Ponemos espacio en blanco entre la tupla.
    cur.execute(query, tupla_datos) #Poner el cursor con el query y la tupla de datos. 

conn.commit() #
conn.close() #Cerrar la base de datos.