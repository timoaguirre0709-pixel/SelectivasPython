cantidad_zapatillas = int(input("Digite la cantidad de zapatillas que comprará: "))
Valor_zapatillas = 20000
total = cantidad_zapatillas*Valor_zapatillas
if cantidad_zapatillas >= 3:
    descuento = total*0.20
    total_descuento = total-descuento
    print(f"El valor de las zapatillas es {total}")
    print(f"El valor de las zapaillas con descuento del 20% es: {total_descuento}")
else:
    descuento = total*0.10
    total_descuento = total-descuento
    print("El valor de las zapatillas es: ",total)
    print(f"Con un descuento de 10% será: {total_descuento}")