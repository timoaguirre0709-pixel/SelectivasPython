PENSION = 100000

promedio = float(input("Promedio del estudiante: "))

porcentaje = 10

if promedio >= 4:
    porcentaje = -30

pago = PENSION + (PENSION * porcentaje / 100)

print(f"Total a pagar: ${pago:.2f}")