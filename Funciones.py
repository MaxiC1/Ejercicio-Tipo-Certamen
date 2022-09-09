import numpy as np

def grabar():
    matriz = []

    continuar = True
    while continuar == True:
        respuesta = input("¿Quiere ingresar una nueva persona? ").lower().strip()#TODO: Mejorar para que la primera vez no pregunte
        if respuesta == "si":
            for i in range (1): #Cantidad de Usuarios
                nombre = input("ingresa Nombre :") #Espacios o Datos dentro del arreglo
                edad = int(input("ingresa edad :"))
                nif = input("ingresa NIF :")

                matriz = np.append(matriz, np.array([[nombre,edad,nif]]), axis=0)
                #mattriz1.append(lista)
                #mattriz1.append(lista2)
                #mattriz1.append(lista3)
                continuar = True
        elif respuesta == "no":
            continuar = False

    print(matriz)
    
    #[[nombre] , [edad] , [nif]] asi se muestra para el lado 
def buscar():
    
    print("Llamó a Buscar")
    
def certificados():
    print("Llamó a Certificados")