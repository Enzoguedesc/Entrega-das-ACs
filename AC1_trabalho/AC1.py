"""
Exercício 1:
 Equações de segundo grau.
- Elabore um código em Python que resolva uma questão de segundo grau ax² + bx + c = 0.
O programa deve ler os parâmetros a, b e c da proposta e deve calcular as raízes pela fórmula de Bhaskara.

Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuários sao sempre númericos.
"""

a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

# Delta
delta = (b ** 2) - 4 * a * c
print("O delta é:", round(delta, 2))

raiz = delta ** 0.5     # Calcular raiz, pode ser tbm math.sqrt(delta) = raiz
print("Raiz quadrada do delta é:", round(raiz, 2))

#Bhaskara
x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz) / (2 * a)
print("x1 =", round(x1, 2))
print("x2 =", round(x2, 2))

# FIM

"""
Exercício 2:
 Anos bissextos.
- Elabore um programa em Python que leia uma variável inteira ano.
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro. No entanto, anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

O programa deve utilizar apenas as funções print(), input()e int(),
além dos operadores lógicos and, or ou not e de operadores aritméticos ou de comparação necessária.
"""

ano = int(input("Informe ano:"))

if(ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
 print(True)
else:
 print(False)

 # FIM