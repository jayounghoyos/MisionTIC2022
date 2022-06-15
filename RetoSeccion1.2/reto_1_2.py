def promediar_notas(notas: list) -> float:
    """
    promediar_notas(notas: list) -> float
    notas: Es de tipo lista, y es la lista de notas del usuario.

    Retornamos un tipo flotante.

    Esta función sirve para promediar los valores de una lista.
    """

    promedio = 0
    for n in notas:
        promedio += n

    return promedio / len(notas)


def obtener_indice_numero_menor(notas: list) -> int:
    """
    {función}
    [{lista_de_parametros}]

    {Lo que retorna}

    {Lo que hace}
    """

    # Index sirve para...
    index = 0
    numero_menor = notas[index]

    # Aquí comparamos...
    for i in range(1, len(notas)):
        if notas[i] < numero_menor:
            numero_menor = notas[i]
            index = i
        else:
            continue

    return index


def formatear_promedio(promedio: float) -> float:
    return round(((5 * promedio) / 100), 2)


if __name__ == "__main__":
    print("Ejercicio Sección 1.2")
    notas = []

    for i in range(1, 6):
        print(f"Dame la nota {i}, por favor: ")
        nota = float(input())
        notas.append(nota)

    indice_para_borrar = obtener_indice_numero_menor(notas)

    notas.pop(indice_para_borrar)

    promedio_notas = formatear_promedio(promediar_notas(notas))

    print(
        f"El promedio ajustado del estudiante es: {promedio_notas}")
