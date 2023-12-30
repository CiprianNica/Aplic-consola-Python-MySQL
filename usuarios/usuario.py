import mysql.connector
import datetime

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Madrid_2014",
    database = "database_aplicacion",
    port = 3306
    )
cursor = con.cursor(buffered=True)
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        cursor.execute(sql, usuario)
        con.commit()
        return [cursor.rowcount, self]
    
    def identificar(self):
        return self.nombre