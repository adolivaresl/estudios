def obtener_valor_absoluto(numero):
    if numero >= 0:
        valor_absoluto = numero
    else:
        valor_absoluto = -numero
    return valor_absoluto

numero = float(input('Ingrese un numero: '))
valor_absoluto = obtener_valor_absoluto(numero)
print(f'El valor absoluto de {numero} es: {valor_absoluto}')