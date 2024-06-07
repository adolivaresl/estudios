def es_nota_valida(nota):
    if 1 <= nota <= 7:
        mensaje = 'La nota es válida'
    else:
        mensaje = 'La nota no es válida'
    return mensaje

nota = float(input('Ingrese una nota: '))
mensaje_validacion = es_nota_valida(nota)
print(mensaje_validacion)