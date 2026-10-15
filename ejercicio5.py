sexo = str(input("Ingrese su sexo (M/F): "))
edad = int(input("Ingrese su edad: "))

if sexo == "M" or sexo == "m":
    num_pulsaciones = (210-edad)/10
    print(f"El numero de pulsaciones es: {num_pulsaciones}")
elif sexo =="F" or sexo == "f":
    num_pulsaciones = (220-edad)/10
    print(f"El numero de pulsaciones es: {num_pulsaciones}")
else:
    print("Ingreso un sexo invalido")