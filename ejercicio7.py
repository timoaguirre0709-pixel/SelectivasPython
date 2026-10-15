llantas = int(input("Ingrese la cantidad de llantas que comprará: "))
if llantas < 5:
    valor_llanta = 300000
elif llantas <= 10:
    valor_llanta = 250000
else:
    valor_llanta = 200000

valor_total = llantas * valor_llanta

print(f"El precio por llanta es: ${valor_llanta}")
print(f"El valor total a pagar es: ${valor_total}")