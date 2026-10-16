PENSION = 100000

promedio = float(input("Promedio del estudiante: "))

porcentaje = 30

if promedio >= 4:
    porcentaje = -50

pago = PENSION + (PENSION * porcentaje / 100)

print(f"Total a pagar: ${pago:.2f}")
