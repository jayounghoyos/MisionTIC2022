def notas_quiz(codigo: str, nota1: float, nota2: float, nota3: float, nota4: float, nota5: float):
    print("El promedio ajustado del estudiante ", {codigo}, " es: ", {
          promedio(nota1, nota2, nota3,  nota4, nota5)})


def promedio(nota1, nota2, nota3,  nota4, nota5):
    return (nota1 + nota2 + nota3 + nota4 + nota5)/5


def menorNum(notas):
    menorNum = 5.1
    for i in notas:
        if i < menorNum:
            menorNum = i
    return menorNum


numVeces = print("Escribe cuantas notas quieres ingresar: ")
for i in numVeces:
    pass
