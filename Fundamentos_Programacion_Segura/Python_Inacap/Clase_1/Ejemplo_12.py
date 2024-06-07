def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def evaluar_aprobacion(promedio):
    if promedio >= 4:
        mensaje = 'Aprobado'
    else:
        mensaje = 'Reprobado'
    return mensaje 

notas = []
for i in range(3):
    nota = float(input(f'ingrese la nota {i + 1}: '))
    notas.append(nota)
    
promedio = calcular_promedio(notas)

mensaje_aprobacion = evaluar_aprobacion(promedio)

print(f'El promedio de las notas es: {promedio: .2f}')
print(f'El estudiante está {mensaje_aprobacion}')