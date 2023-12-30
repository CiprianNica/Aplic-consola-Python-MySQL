import mysql.connector
import datetime
import hashlib

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Madrid_2014",
    database = "database_aplicacion",
    port = 3306)
cursor = con.cursor(buffered=True)

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        
        # cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            con.commit()
            result = [cursor.rowcount, self]
        except mysql.connector.errors.IntegrityError:
            result = [0, self]
        return result
    
    def identificar(self):
        return self.nombre