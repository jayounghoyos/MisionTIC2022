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


codigo = input("Bienvenido, digita tu codigo: ")

nota1 = float(input("Bienvenido, digita la primera nota: "))
nota2 = float(input("Bienvenido, digita la segunda nota: "))
nota3 = float(input("Bienvenido, digita la tercera nota: "))
nota4 = float(input("Bienvenido, digita la cuarta nota: "))
nota5 = float(input("Bienvenido, digita la quinta nota: "))

notas = [round(nota1, 2), round(nota2, 2), round(
    nota3, 2), round(nota4, 2), round(nota5, 2)]
notas = [round(nota1, 2), round(nota2, 2), round(
    nota3, 2), round(nota4, 2), round(nota5, 2)]
notas = notas.remove(menorNum)

print("Tus notas son: ", notas, " y la menor de ellas es: ", menorNum(notas))
notas_quiz(codigo, nota1, nota2, nota3,  nota4, nota5)
