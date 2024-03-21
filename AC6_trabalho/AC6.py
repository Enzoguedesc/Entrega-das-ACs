# 1000
print("Hello World!")


# 1001
a = int(input())
b = int(input())


x = a + b
print("X =", x)


# 1010
peca01 = input().split()
peca02 = input().split()

codigo_peca01 = int(peca01[0])
codigo_peca02 = int(peca02[0])

numero_peca01 = int(peca01[1])
numero_peca02 = int(peca02[1])

valor_unitario_peca01 = float(peca01[2])
valor_unitario_peca02 = float(peca02[2])

valor_peca01 = numero_peca01 * valor_unitario_peca01
valor_peca2 = numero_peca02 * valor_unitario_peca02

total = valor_peca01 + valor_peca2

print(f"VALOR A PAGAR: R$ {total:.2f}")


# 1013
a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a - b)) / 2
if maiorAB < c:
    maiorAB = c

print('{:.0f}'.format (maiorAB), 'eh o maior')


# 1015
x1, y1 = map(float, input().split())

x2, y2 = map(float, input().split())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("{:.4f}".format(distancia))