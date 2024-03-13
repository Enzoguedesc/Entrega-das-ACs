'''
Exercicio 01 - revisitar um AC1
- eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma descoberta de segundo grau no formato
ax² + bx + c = 0, supondo as raízes sempre reais;
- bissexto(ano), que recebe um valor inteiro e retorna um valor booleano,
informando se o ano é bissexto ou não.
'''

def eq_seg_grau(a, b, c):
    delta = (b ** 2) - 4 * a * c
    return (-b + (delta ** 0.5)) / (2 * a), (-b - (delta ** 0.5)) / (2 * a)

#Teste
print(eq_seg_grau(1, -2, -3))  # (3.0, -1.0)
print("-" * 30)
print(eq_seg_grau(1, -6, 8))   # (4.0, 2.0)


print("-" * 30)


def ano(x):
    if(x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
        return True
    return False

#Teste
print(ano(1900))  # False
print(ano(1995))  # False
print(ano(2000))  # True
print(ano(2012))  # True

print("-" * 30)

'''
Exercício 2: salário
- Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe duas configurações posicionais reais, valor_horae num_horas,
que exigem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente.
Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275.
A função retorna o salário líquido de um funcionário, calculada como o produto do valor por hora em número de horas,
limitado o percentual do imposto de renda dado.
'''

def calcula_salario(valor_horae, num_horas):
    return (valor_horae * num_horas) * 0.275

#Teste
print(round(calcula_salario(400, 30), 2))    # 3300.0
print(round(calcula_salario(150, 40), 2))    # 1650.0
print(round(calcula_salario(1000, 15), 2))   # 4125.0
print(round(calcula_salario(1000, 15), 2))   # 4125.0