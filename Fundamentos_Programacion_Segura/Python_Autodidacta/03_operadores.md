<div align="center">
  <h1> Apuntes de Python </h1>
  <sub> Autor:
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank"> David Villegas</a><br>
  <small> Edición: Mayo, 2024, Chile</small>
</div>

-----

## OPERADORES DE ASIGNACIÓN

Los operadores de asignación se utilizan para asignar valores a variables. -

| OPERADOR       | EJEMPLO        | IGUAL QUE       |
| --------       | -------        | -------         |
|  `=`           |  X = 5         |  X = 5          |
|  `+=`          |  X + = 3       |  X = X + 3      |
|  `-=`          |  X - = 3       |  X = X - 3      |
|  `*=`          |  X * = 3       |  X = X * 3      |
|  `/=`          |   X / = 3      |  X = X / 3      |
|  `%=`          |  X % = 3       |  X = X % 3      |
|  `//=`         |  X // = 3      |  X = X // 3     |
|  `**=`         |  X ** = 3      |  X = X ** 3     |
|  `&=`          |  X & = 3       |  X = X & 3      |
|  `|=`          |  X | = 3       |  X = X | 3      |
|  `^=`          |  X ^ = 3       |  X = X ^ 3      |
|  `>>=`         |  X >> = 3      |  X = X >>3      |
|  `<<=`         |  X << =        |  X = X <<3      |
|                |                |                 |

## OPERADORES ARITMETICOS

| OPERADOR | NOMBRE | EJEMPLO |
| -------- | ------ | ------- |
| `+`          | Suma                  | X + Y        |
| `-`          | Resta                 | X - Y        |
| `*`          | Multiplicación        |  X * Y       |
| `/`          | División              | X / Y        |
| `%`          | Modulo                | X % Y        |
| `**`         | Exponenciacion        | X ** Y       |
| `//`         | Division de enteros   | X // Y       |

*Ejemplo:*

```py
print(suma:, 1 + 2)             # Salida 3
print(resta:, 2 - 1)            # Salida 1
print(multiplicacion:, 2 * 3)   # Salida 6
print(division:, 4 / 2)         # Salida 2.0
print(modulo:, 3 % 2)           # Salida 1
print(exponenciacion:, 2 ** 3)  # Salida 9
```
-----

## OPERADORES DE COMPARACION

En programación comparamos valores, usamos operadores de comparación para comparar dos valores. Comprobamos si un valor es mayor, menor o igual a otro valor.

| OPERADOR      | NOMBRE                  | EJEMPLO        |
| --------      | ------                  | -------        |
|   `==`        |   Igual                 |   X = = Y      |
|   `!=`        |   No es igaul           |  X ! = Y       |
|   `>`         |  Mayor que              |   X > Y        |
|   `<`         |  Menor que              |  X < Y         |
|   `>=`        |  Mayor o igual que      |  X > = Y       |
|   `<=`        |   Menor o igual que     |  X < = Y       |

*Ejemplo:*
```py
print(3 > 2)                            # True, Verdadero ya que 3 es mayor que 2.
print(3 >= 2)                           # True, Veradero, ya que 3 es mayor que 2.
print(3 < 2)                            # False, Falso por que 3 es mayor que 2.
print(2 < 3)                            # True, Verdadero por que 2 es menor que 3.
print(2 <= 3)                           # True, Verdadero por que 2 es menor que 3
print(3 == 2)                           # False, Porque 3 no es igual a 2.
print(3 != 2)                           # True, Porque 3 no es igual a 2.
print(len('mango') == len('avocado'))   # False, 
print(len('mango') != len('avocado'))   # True, 
print(len('mango') < len('avocado'))    # True
print(len('milk') != len('meat'))       # False

```
-----

## OPERADORES LOGICOS

A diferencia de otros lenguajes de programación Python utiliza palabras clave y, o y no para operadores lógicos. Los operadores lógicos se utilizan para combinar declaraciones condicionales:

### OPERADOR `AND`

Se utiliza para combinar dos o mas expresiones booleanas y solo devuelve `True` si **todas** las expresiones son `True`, si al menos una expresion es `False`, el resultado final será `False`. 

*Ejemplo*

```PY
X < 5 and X < 10 
```
-----

### OPERADOR `OR`

Se utiliza para evaluar dos o más expresiones booleanas y devolver un resultado final de `True` o `False`, su funcionamiento se basa en la siguiente logica:

- Si al menos una de las expresiones booleanas evaluadas es `True`, el resultado final de la operacion `or` será `True`.
- Solo si todas las expresiones booleanas evaluadas son `False`, el resultado final de la operación `or` será `False`.

*Ejemplo*
```py
esta_lloviendo = True
tiene_paraguas = False
necesita_paraguas = esta_lloviendo or tiene_paraguas
print(necesita_paraguas) # Imprime True
```
-----

### OPERADOR `NOT`
El operador logico `not` en python se utiliza para negar o invertir el valor de una expresión booleana. en otras palabras, toma una expresión booleana como entrada y devuelve el valor opuesto.

*Ejemplo:*
```PY
esta_lloviendo = True
no_esta_lloviendo = not esta_lloviendo
print(no_esta_lloviendo) # Imprime False
```

-----
<div align="center">Code With ❤️ Trebol <div>
<small> Edición: Mayo, 2024</small><br>


<div align="center">
  <a href="https://www.instagram.com/treboldev/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="instagram logo"  />
  </a>
  <a href="https://discord.com/trebol_dev" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="discord logo"  />
  </a>
  <a href="<dpvc.chile@gmail.com>" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="gmail logo"  />
  </a>
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin logo"  />
  </a>
  <a href="https://www.facebook.com/VJTrebol.CL" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Facebook&logo=facebook&label=&color=1877F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="facebook logo"  />
  </a>
  <a href="https://x.com/treboldev" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="twitter logo"  />
  </a>
</div>