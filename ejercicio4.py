total_compra = int(input("Ingrese el total de su compra: "))
color = input("Ingrese el color de la balota: ")

match color:
    case "rojo":
        descuento = total_compra*0.15
        total_descuento = total_compra-descuento
        print(f"El total de su compra es de {total_compra}, pero con un descuento ({descuento}) del 15% por ser una boleta roja sera de {total_descuento}")
    case "verde":
         descuento = total_compra*0.20
         total_descuento = total_compra-descuento
         print(f"El total de su compra es de {total_compra}, pero con un descuento ({descuento}) del 20% por ser una boleta verde sera de {total_descuento}")
    case _:
        print(f"El total de su compra será de {total_compra} por no tener una boleta valida")
