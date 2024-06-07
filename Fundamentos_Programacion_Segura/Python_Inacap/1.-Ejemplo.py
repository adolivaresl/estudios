print('Hola mundo')

#Ejemplo de variable string y concatenación 
nombre = 'David'
print('Hola', nombre)

#Funcion Imput
nombre = input('ingrese su nombre: ')
print('Hola', nombre)                   #Output: Hola, <nombre ingresado por usuario>

#Ingresar número entero
numero_entero = int(input('Ingrese un número entero: '))
print('El numero entero ingresado es:', numero_entero)

#Ingresar número flotante
numero_flotante = float(input('Ingrese un número flotante: '))
print('El numero flotante ingresado es: ', numero_flotante)

#Suma de dos números ingresados por el usuario.
numero1 = int(input('Ingresar el primer número entero: '))
numero2 = int(input('Ingrese el segundo numero entero: '))

suma = numero1 + numero2

print('La suma de', numero1, 'y', numero2, 'es igual a:', suma)

# EJERCICIO 1
centimetro = int(input('Ingrese los centimetros a calcular: '))
pulgadas = centimetro * 2.54
print('los centimetros ingresados corresponden a: ',pulgadas)

#EJERCICIO 2
base = int(input('Ingresa la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))
area = base * altura
print('El area del rectangulo corresponde a: ', area)

#EJERCICIO 3
num_entero = int(input('Ingrese un numero entero a calcular: '))
cuadrado = num_entero * num_entero
print('El cuadrado del numero ingresado corresponde a: ',cuadrado)

#EJERCICIO 4
base_tri = int(input('Ingrese la base del triangulo: '))
altura_tri = int(input('Ingrese la altura del triangulo: '))
area_tri = base_tri * altura_tri / 2
print('El area del triangulo es: ', area_tri)

#EJERCICIO 5
grados = int(input('Ingrese los grados celcius a calcular'))
G_Fah = grados * 9 / 5 + 32
print('Los grados celcius ingresados corresponden a :',G_Fah, 'Grados Fahrenheit')

#EJERCICIO 6
km = int(input('Ingrese los kilometros a calcular: '))
millas = km * 0.621371
print('Los kilometros ingresados corresponden a :', millas, 'Millas')

#EJERCICIO 7
Nom_Con = input('Ingrese su nombre :')
print('Hola ',Nom_Con, 'Ten un excelente dia !')

#EJERCICIO 8
num_prom1 = int(input('Ingrese el primero número entero a calcular: '))
num_prom2 = int(input('Ingrese el segundo numero entero a calcular :'))
num_prom3 = int(input('Ingrese el tercer numero entero a calcular: '))

prom = num_prom1 + num_prom2 + num_prom3 / 3
print('El promedio de los 3 números ingresados corresponde a :', prom)

