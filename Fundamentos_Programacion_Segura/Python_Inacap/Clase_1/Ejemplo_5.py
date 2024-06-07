# EJERCICIO 5
# Solicite al usuario una temperatura en grados Celsius y luego imprima su equivalente en grados Fahrenheit (fórmula: Fahrenheit = Celsius * 9 / 5 + 32)

grados = int(input('Ingrese los grados celcius a calcular: '))
G_Fah = grados * 9 // 5 + 32
print('los grados celcius ingresados corresponden a : ', G_Fah, 'Grados Fahrenheit')