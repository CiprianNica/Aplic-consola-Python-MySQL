import usuarios.usuario as modelo

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
        
        email = input("tu email: ")
        password = input("tu contraseña: ")
        
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        
        if email == login[3]:
            print(f"bienveido {login[1]}, te has registrado en el sist el {login[5]}")
        else:
            print("no hay este usuario...")
        print(login)