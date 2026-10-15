valor_total = float(input("Ingrese el monto total de la compra: $"))

if valor_total > 500000:
    valor_propio = valor_total * 0.55
    valor_banco = valor_total * 0.30
    valor_credito = valor_total * 0.15
else:
    valor_propio = valor_total * 0.70
    valor_banco = 0
    valor_credito = valor_total * 0.30

interes = valor_credito * 0.20
valor_total_credito = valor_credito + interes

print(f"Dinero propio: ${valor_propio}")
print(f"Préstamo del banco: ${valor_banco}")
print(f"Crédito solicitado al fabricante: ${valor_credito}")
print(f"Interés del crédito (20%): ${interes}")
print(f"Total del crédito con intereses: ${valor_total_credito}")