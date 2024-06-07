


#ALTERNATIVA 2 - MEDIANTE FUNCION

def es_positivo_o_negativo(numero):
    if numero > 0:
        mensaje = 'El numero es positivo'
    elif numero == 0:
        mensaje = 'El numero es cero'
    else:
        mensaje = 'El número es negativo'
    return mensaje

numero = float(input('Ingrese un número: '))
mensaje = es_positivo_o_negativo(numero)
print(mensaje)
