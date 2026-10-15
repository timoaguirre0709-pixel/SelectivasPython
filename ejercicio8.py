edad = float(input("Ingrese la edad: "))
unidad_edad = input("Ingrese la unidad de edad (Meses o Años): ").strip().lower()

if unidad_edad == "meses":
    edad = edad / 12
elif unidad_edad == "años":
    edad = edad
else:
    print("Unidad no válida. Debe ingresar Meses o Años.")
    exit()

hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

if edad <= 1/12:
    rango_min = 13
    rango_max = 26
elif edad <= 6/12:
    rango_min = 10
    rango_max = 18
elif edad <= 1:
    rango_min = 11
    rango_max = 15
elif edad <= 5:
    rango_min = 11.5
    rango_max = 15
elif edad <= 10:
    rango_min = 12.6
    rango_max = 15.5
elif edad <= 15:
    rango_min = 13
    rango_max = 15.5
else:
    sexo = input("Ingrese el sexo (M para hombre o F para mujer): ").upper()
    if sexo == "M":
        rango_min = 14
        rango_max = 18
    elif sexo == "F":
        rango_min = 12
        rango_max = 16
    else:
        print("Sexo incorrecto")
        exit()

if hemoglobina < rango_min:
    print("Resultado: positivo")
    print(f"Nivel de hemoglobina: {hemoglobina} g%")
    print(f"Rango esperado: {rango_min} - {rango_max} g%")
    print("La persona presenta anemia.")
else:
    print("Resultado: negativo")
    print(f"Nivel de hemoglobina: {hemoglobina} g%")
    print(f"Rango esperado: {rango_min} - {rango_max} g%")
    print("La persona no presenta anemia.")
