def es_par_o_impar(numero):
    if numero % 2 == 0:
        mensaje = 'El número es par'
    else:
        mensaje = 'El número es impar'
    return mensaje

numero = int(input('Ingrese un número: '))
mensaje_paridad = es_par_o_impar(numero)
print(mensaje_paridad)