# EJERCICIO 4
# Solicite al usuario la base y altura de un triángulo, luego calcule el área de éste, Area = base * altura / 2

base_tri = int(input('Ingrese la base del triangulo: '))
altura_tri = int(input('Ingrese la altura del triangulo: '))
area_tri = (base_tri * altura_tri) // 2
print('El area del triangulo es: ', area_tri)