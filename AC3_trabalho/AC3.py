"""
Exercício 1: triângulos
Desenvolve uma função determina_tipo_trianguloque recebe três lados de um triângulo e retorna uma string,
"Escaleno", "Isósceles"ou "Equilátero", conforme o tipo do triângulo.
A função deve retornar "Não é um triângulo"se os três lados não formarem um triângulo.
"""
def determina_tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilatero"
    if l2 == l3:
        return "Isósceles"
    if l1 != l2 != l3:
        return "Escaleno"
    return "Não é um triângulo"

print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo


"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que obtém um número inteiro e retorna uma string
decrescente o dia da semana equivalente, considerando que o dia da semana igual a 1 é o domingo,
2 é segunda-feira, etc. seja inválido.
"""
def dia_semana(x):
    if x == 1:
        return "Domingo"
    if x == 2:
        return "Segunda-Feira"
    if x == 3:
        return "Terca-Feira"
    if x == 4:
        return "Quarta-Feira"
    if x == 5:
        return "Quinta-Feira"
    if x == 6:
        return "Sexta-Feira"
    if x == 7:
        return "Sábado"
    return "Dado inválido"

print(dia_semana(3)) # Terca-feira
print(dia_semana(4)) # quarta-feira
print(dia_semana(5)) # quinta-feira
print(dia_semana(10)) # Dado inválido


"""
Exercício 3: calculadora simples
Desenvolve funções de operações aritméticas soma, subtracao, multiplicacaoe divisao,
que recebem dois números cada uma e retornam o resultado da operação indicada.
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI),
que lê dois números e uma operação e exibe na tela o valor do resultado,
ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações .
"""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def cli():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    x = input("Escolha uma operação:")
    if x == "soma":
        resultado = a + b
        print("O resultado da adição é:", resultado)
    if x == "subtracao":
        resultado = a - b
        print("O resultado da subtração é:", resultado)
    if x == "multiplicacao":
        resultado = a * b
        print("O resultado da multiplicação é:", resultado)
    if x == "divisao":
        resultado = a / b
        print("O resultado da divisão é:", resultado)
    else:
        print("Operação inválida!")

cli()
