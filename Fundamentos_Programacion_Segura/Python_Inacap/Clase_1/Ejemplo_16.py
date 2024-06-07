def mostrar_de_menor_a_mayor(numero1, numero2):
    if numero1 <= numero2:
        menor = numero1
        mayor = numero2
    else:
        menor = numero2
        mayor = numero1
    
    print(f'El número menor es: {menor}')
    print(f'El número mayor es: {mayor}')
    
numero1 = float(input('Ingrese el primer número: '))
numero2 = float(input('Ingrese el segundo número: '))

mostrar_de_menor_a_mayor(numero1, numero2)