from usuarios import acciones
print("""
Acciones disponibles:
    - registro(r)
    - login(l)
""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer? ")

if accion.lower() == "r":
    hazEl.registro()
elif accion.lower() == "l":
    hazEl.login()
else:
    print("Opcion eronea ...")

