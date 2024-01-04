import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"\nOK, {usuario[1]} vamos a crear una nueva nota...")
        titulo = input("Titulo nota: ")
        description = input("Introduce tu nota: ")
        
        # crear el objeto(llamar modelo de nuestra nota)
        nota = modelo.Nota(usuario[0], titulo, description)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\nHAS GUARDADO LA NOTA: {nota.titulo}")
        else:
            print(f"\nSiento {usuario[1]}, no se ha guardado la nota.")
            
    def mostrar(self, usuario):
        print(f"Vamos a mostrar las notas del usuario {usuario[1]}")
        #crear el objeto
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print(nota)
    
    def borrar(self, usuario):
        print(f"\nOK {usuario[1]}, vamos a borrar notas..")
        titulo = input("Introd titulo de la nota a borrar: ")
        # crear el objeto
        nota = modelo.Nota(usuario[0], titulo)
        #borrar nota con titulo introducido
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print(f"{usuario[1]}, no se ha borrado la nota {nota.titulo}")  