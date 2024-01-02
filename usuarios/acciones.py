import usuarios.usuario as modelo
from usuarios.errores import ErrorPassword, ErrorEmail

class Acciones:
    
    def registro(self):
        print("\nok, vamos a registrarte en el sistema...")
        
        nombre = input("Introduce tu nombre: ")
        apellidos = input('Introduce tus apellidos: ')
        email = input("tu email: ")
        password = input("tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}.")
        else:
            print("\nNo te has registrado correctamente !!")
        
    def login(self):
        print("\nvale, identificate en el sistema...")
        #try:
        email = input("tu email: ")
        password = input("tu contraseña: ")
                
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        if login != None:
            print("Login exitoso!!")
        else:
            print("Error, email o password incorrectos.")            
    def proximasAcciones(self, usuario):
        return None