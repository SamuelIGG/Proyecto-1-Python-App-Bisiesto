

año = input("Escribe el año que quieres verificar: ")

if int(año) % 4 != 0: 
    print("No es bisiesto") 
elif int(año) % 4 == 0 and int(año) % 100 != 0:
    print("Es bisiesto") 
elif int(año) % 4 == 0 and int(año) % 100 == 0 and int(año) % 400 != 0: 
    print("No es bisiesto") 
elif int(año) % 4 == 0 and int(año) % 100 == 0 and int(año) % 400 == 0: 
    print("Es bisiesto")

