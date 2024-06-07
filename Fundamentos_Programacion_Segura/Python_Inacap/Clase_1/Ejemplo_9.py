# EJERCICIO 9
# Por ser un día especial se dará un 5% de descuento a todos los productos vendidos, solicite un precio e imprima el valor de venta aplicando el 5% de descuento

precio = float(input('Ingrese el precio del producto: '))
descuento = precio * 0.05
precio_final = precio - descuento

print('El precio final con el 5% de descuento es de: ', precio_final)


# ALTERNATIVA 2 - CREADA A PARTIR DE UNA FUNCION

def calcular_descuento(precio):
    descuento = precio * 0.05
    precio_final = precio - descuento
    return precio_final

precio = int(input('Ingrese el precio del producto: '))
precio_final = calcular_descuento(precio)
print(f'El precio final con el 5% de descuento es de: ${precio_final:2f}')
