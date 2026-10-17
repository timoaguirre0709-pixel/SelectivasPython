promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pensión: "))

if promedio >= 4.0:
    descuento = pension * 0.30
    total = pension - descuento
    print("Tiene un descuento del 30%.")
    print("Total a pagar:", total)

elif promedio >= 0 and promedio < 4.0:
    iva = pension * 0.10
    total = pension + iva
    print("Debe pagar la pensión completa más el IVA.")
    print("Total a pagar:", total)

else:
    print("Error: el promedio no puede ser negativo.")
