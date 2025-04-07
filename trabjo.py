
import random

def generar_numeros_aletorio(rango,cantidad):

    nombre = input("Ingresar Nombre: ")



    numeros_posibles = set(range(0, rango ))
    
    numeros_generados = []
    
    while len(numeros_generados) < cantidad and numeros_posibles:
        numero = random.choice(list(numeros_posibles))
        
        
        if numero < 0:
           continue
       
        numeros_generados.append(numero)
        numeros_posibles.remove(numero)
        
        
    return [f"{num:02d}" for num in numeros_generados] 

rango = 10
cantidad = 5

numero = generar_numeros_aletorio(rango,cantidad)
print(f" tus numeros son: {numero}")

