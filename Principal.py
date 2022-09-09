import Funciones as fn

def menu():
    continuar = True
    print("Bienvenido:")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir Certificado")
    print("4. Salir")

    opcion = input("Ingrese la opción: ")
    if opcion == "1": fn.grabar()
    elif opcion == "2": fn.buscar()
    elif opcion == "3": fn.certificados()
    elif opcion == "4": continuar = False

    return continuar

while menu(): pass