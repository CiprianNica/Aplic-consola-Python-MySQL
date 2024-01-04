import usuarios.usuario as modelo
import notas.acciones

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
            self.proximasAcciones(usuario)
        else:
            print("\nNo te has registrado correctamente !!")
        
    def login(self):
        print("\nvale, identificate en el sistema...")
        #try:
        email = input("tu email: ")
        password = input("tu contraseña: ")
                
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        print(login)
        if login != None:
            print("Login exitoso!!")
            print(f"Bienvenido {login[1]} !!")
            self.proximasAcciones(login)
        else:
            print("Error, email o password incorrectos.")   

    def proximasAcciones(self, usuario):
        print("""
        Accones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)
        accion = input("Que quieres hacer? ")
        hazEl = notas.acciones.Acciones()
        if accion == "crear":
            notas.acciones.Acciones().crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            print("vamos a salir...")
            exit()
        else: 
            print("la opcion elejida no es valida")
            self.proximasAcciones(usuario)