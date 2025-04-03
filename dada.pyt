import time 

def menu_interativo():
    while True:
        print("Menu de opcion: ")
        print("1. Realizar accion 1")
        print("2. Realizar accion 2")
        print("3. Salir")
        
        opcion = input("Elige una opcion (1-3): ")
        
        if opcion == "1":
            print("Realizando accion 1...")
            time.sleep(1)
            
        elif opcion == "2":
             print("Realizando accion 2...")
             time.sleep(1)
             
        elif opcion == "3":
            print("Saliendo de programa...")
            time.sleep(2)
            break
        else:
            print("Opcion no valida. Intente con una opcion valida (1-3).")

menu_interativo()