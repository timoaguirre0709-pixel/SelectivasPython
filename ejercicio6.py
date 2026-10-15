promedio = float(input("Ingrese la calificación del periodo pasado: "))
pension = float(input("Ingrese el valor de la pensión: "))
if promedio >= 4:
    descuento = pension*0.30
    total_pension = pension-descuento
    print(f"Por su buen rendimiento, se le dara un 30% de descuento, por lo que su pensión sera de: {total_pension}")
else:
    iva = pension*0.10
    total_pension = pension+iva
    print(f"El alumno debera pagar una pension de {total_pension} más un 10% de iva que equivale a {iva}")