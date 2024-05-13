#1016
distancia = int(input())
def caulcular_tempo(distancia, velocidade_x, velocidade_y):
    tempo = distancia / (velocidade_y - velocidade_x)
    return tempo * 60

tempo = caulcular_tempo(distancia, 60, 90)

print(f"{tempo:.0f} minutos")

# 1153
import math

numero = int(input())

resultado = math.factorial(numero)

print(resultado)

# 1281

n = int(input())
for _ in range(n):
    m = int(input())
    produtos = {}
    for _ in range(m):
        produto, preco = input().split()
        produtos[produto] = float(preco)
    p = int(input())
    total = 0
    for _ in range(p):
        produto, quantidade = input().split()
        total += produtos[produto] * int(quantidade)
    print(f"R$ {total:.2f}")


# 2006

t = int(input())
respostas = list(map(int, input().split()))
resposta_correta = 0
for resposta in respostas:
    if resposta == t:
        resposta_correta += 1
print(resposta_correta)


# 2339

c, p, f = map(int, input().split())
if c * f <= p:
    print("S")
else:
    print("N")


# 2388

n = int(input())
distancia = 0
for _ in range(n):
    t, v = map(int, input().split())
    distancia += t * v
print(distancia)


# 2413

num_pessoas = int(input())
quantidade = num_pessoas * 4
print(quantidade)


# 3048

def num_maximo_marcado(N, V):
    marcado = 1
    marca_anterior = V[0]

    for i in range(1, N):
        if V[i] != marca_anterior:
            marcado += 1
            marca_anterior = V[i]

    return marcado

N = int(input())
V = [int(input()) for _ in range(N)]

print(num_maximo_marcado(N, V))