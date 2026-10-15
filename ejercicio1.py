nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
promedio = (nota1+nota2+nota3)/3

if promedio >= 70:
    print("Aprobaste :)")
else:
    print("No aprobaste :(")