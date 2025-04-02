import random

def generar_numeros_aletorio(rango,cantidad):
    numeros_generados = set()
    while len(numeros_generados) < cantidad:
        numero = random.randint(1,rango)
        
        
        if numero < 10:
           continue
        numeros_generados.add(numero)
    return list(numeros_generados)

rango = 100
cantidad = 5

numero = generar_numeros_aletorio(rango,cantidad)
print(f"{numero}")

