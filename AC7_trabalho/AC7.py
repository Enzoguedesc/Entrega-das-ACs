
# 1048
salario = float(input())

if salario <= 400.00:
    novo_salario = salario + salario * 0.15
    reajuste_ganho = salario * 0.15
elif salario <= 800.00:
    novo_salario = salario + salario * 0.12
    reajuste_ganho = salario * 0.12
elif salario <= 1200.00:
    novo_salario = salario + salario * 0.10
    reajuste_ganho = salario * 0.10
elif salario <= 2000.00:
    novo_salario = salario + salario * 0.07
    reajuste_ganho = salario * 0.07
else:
    novo_salario = salario + salario * 0.04
    reajuste_ganho = salario * 0.04

percentual = (reajuste_ganho / salario) * 100
    


print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {percentual:.0f} %')



# 1065
seguencia_valores = []
for i in range(5):
    valores = int(input())
    seguencia_valores.append(valores)

quantidade_valores = 0
for valores in seguencia_valores:
    if valores % 2 == 0:
        quantidade_valores += 1

print(quantidade_valores, 'valores pares')



# 1132
X = int(input())
Y = int(input())

soma = 0
if X < Y:
    for i in range(X, Y+1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(Y, X+1):
        if i % 13 != 0:
           soma += i

print(soma)



# 1173
V = int(input())
N = [0] * 10
N[0] = V

for i in range(1, 10):
    N[i] = N[i -1] * 2

for i in range(10):
    print("N[%d] = %d" % (i, N[i]))



# 1180
N = int(input())
X = list(map(int, input().split()))

valor_minimo = X[0]
posicao = 0
for i in range(1, N):
    if X[i] < valor_minimo:
        valor_minimo = X[i]
        posicao = i

print('Menor valor:', valor_minimo)
print('Posicao:', posicao)


#1182
C = int(input())
T = input().upper()

M = []
for i in range(12):
    row = list(map(float, input().split()))
    M.append(row)

area_verde = []
for i in range(2, 6):
    area_verde.append(M[i][C-1])
for i in range(7, 11):
    area_verde.append(M[i][C-1])

total = sum(area_verde)
media = total / len(area_verde)

if T == 'S':
    print("{:.1f}".format(total))
elif T == 'M':
    print("{:.1f}".format(media))

# 1244
N = int(input())

for i in range(N):
    strings = input().split()

    strings.sort(key=len)

    for j in range(len(strings)):
        print(strings[j], end=" ")
    print()