#Utilice una sola condicion if, para evitar rebundancias, y hacer el codigo más simple, además de intercambiar los porcentajes, donde originalmente era un 10% de IVA y lo cambie por un 30%, mientras que el descuento que hice fue de un 50% para incentivar aun más a los estudiantes
#Lo cambie de esta manera porque en el ejercicio original tambien agregaba un else, mientras que en este solo agregue una condicion if
#Dependiendo de el promedio del estudiante se le agregara o rebajara al pago de la pension, siendo este un 30% de más siempre y cuando saque menos de 4 o más, mientras que un descuento de 50% si logra alcanzar un promedio mayor o igual a 4
PENSION = 100000

promedio = float(input("Promedio del estudiante: "))

porcentaje = 30

if promedio >= 4:
    porcentaje = -50

pago = PENSION + (PENSION * porcentaje / 100)

print(f"Total a pagar: ${pago:.2f}")
