import mysql.connector

def conectar():
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Madrid_2014",
        database = "database_aplicacion",
        port = 3306)
    cursor = con.cursor(buffered=True)
    return [con, cursor]