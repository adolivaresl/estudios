#EJERCICIO 13
# .Solicite al usuario la cantidad de hijos de un empleado: a. Si el usuario tiene menos de tres hijos se dará un bono de 50000 por cada hijo b. Si tiene más de dos hijos se dará un bono de 30000 por cada hijo Al finalizar, Muestre el valor total del bono a dar

def calcular_bono(cantidad_hijos):
    if cantidad_hijos < 3:
        bono_por_hijo = 50000
    else:
        bono_por_hijo = 30000
        
    bono_total = cantidad_hijos * bono_por_hijo
    return bono_total

cantidad_hijos = int(input('Ingrese la cantidad de hijos del empleado: '))
bono_total = calcular_bono(cantidad_hijos)
print(f'El valor total del bono a otorgar es de: {bono_total}')