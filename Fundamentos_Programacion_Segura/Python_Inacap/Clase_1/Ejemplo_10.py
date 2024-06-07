# EJERCICIO 10
# Solicite al usuario un valor correspondiente a un tiempo medido en horas y muestre el valor en minutos (EJ: 1.5 horas = 90 min)

horas = float(input('Ingrese un valor en horas: '))
minutos = horas * 60
print('Las horas ingresadas equivalen a: ',minutos, 'minutos')


# ALTERNATIVA 2 - MEDIANTE FUNCION
def horas_a_minutos(horas):
    minutos = horas * 60
    return minutos

horas = float(input('Ingrese un valor en horas: '))
minutos = horas_a_minutos(horas)
print(f'{horas} Las horas ingresadas equivalen a {minutos} minutos')