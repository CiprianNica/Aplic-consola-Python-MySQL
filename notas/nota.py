
#conectar con la bd
import usuarios.conexion as conexion

conect = conexion.conectar()
database = conect[0]
cursor = conect[1]

# crear modelo
class Nota:
    def __init__(self, usuario_id, titulo='', description=''):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.description = description
        
    def guardar(self):
        sql = "INSERT INTO notas(usuario_id, titulo, description, fecha) VALUES(%s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.description)
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
    
    def listar(self):
        sql = "SELECT * FROM notas WHERE usuario_id = %s"
        usuario = (self.usuario_id,)
        cursor.execute(sql, usuario)
        result = cursor.fetchall()
        return result
    
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '{self.titulo}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
    
        
    