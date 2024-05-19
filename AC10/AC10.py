# 1258
caso1 = True

while True:
    n = int(input())
    if n == 0:
        break

    camisetas = []

    for _ in range(n):
        nome = input()
        cor, tamanho = input(). split()
        camisetas.append((cor, tamanho, nome))

    camisetas.sort(key=lambda x: (x[0], -ord(x[1]), x[2]))

    if not caso1:
        print()
    for cor, tamanho, nome in camisetas:
        print(cor, tamanho, nome)

    caso1 = False

# 1260
n = int(input())
input()

for i in range(n):
    if i > 0:
        print()

    madeiras = {}

    try:
        while True:
            madeira = input()
            if not madeira:
                break

            if madeira in madeiras:
                madeiras[madeira] += 1 
            else:
                madeiras[madeira] = 1
    except EOFError:
        pass

    total = sum([qtd for qtd in madeiras.values()])

    for madeira in sorted(list(madeiras.keys())):
        print(f"{madeira} {(100*madeiras[madeira] / total):.4f}")

    
# 2518
import math

while True:
    try:
        n = int(input())
    except EOFError:
        break

    h, c, l = input().split()

    baseRampa = int(c) * int(n)
    alturaRampa = int(h) * int(n)
    larguraRampa = l

    comprimentoRampa = math.sqrt(alturaRampa ** 2 + baseRampa ** 2)

    areaRampa = float(larguraRampa) * float(comprimentoRampa)

    print(f"{areaRampa / 10000:.4f}")