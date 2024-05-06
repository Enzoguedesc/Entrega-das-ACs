# 1028
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
for _ in range(N):
    F1, F2 = map(int, input().split())
    print(mdc(F1, F2))

#1087
def movimentacao(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx == 0 or dy == 0:
        return 1
    elif dx == dy:
        return 1
    else:
        return 2

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    print(movimentacao(x1, y1, x2, y2))

# 1161
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

while True:
    try:
        m, n = map(int, input().split())
        print(factorial(m) + factorial(n))
    except EOFError:
        break


# 1170
n = int(input())
for _ in range(n):
    c = float(input())
    dias = 0
    while c > 1:
        c -= c / 2
        dias += 1
    print(f"{dias} dias")

#1171
n = int(input())

quantidade = {}

for _ in range(n):
    x = int(input())
    if x in quantidade:
        quantidade[x] += 1
    else:
        quantidade[x] = 1

for numero, quantas in sorted(quantidade.items()):
    print(f'{numero} aparece {quantas} vez(es)')

#1221
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    if is_prime(x):
        print("Prime")
    else:
        print("Not Prime")

# 1329
def cara_ou_coroa():
    while True:
        n = int(input())
        if n == 0:
            break
        resultado = list(map(int, input().split()))
        john_ganhou = sum(resultado)
        maria_ganhou = n - john_ganhou
        print(f"Mary won {maria_ganhou} times and John won {john_ganhou} times")

if __name__ == "__main__":
    cara_ou_coroa()

# 1555
def max_funcao():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        r = (3 * x) ** 2 + y ** 2
        b = 2 * (x ** 2) + (5 * y) ** 2
        c = -100 * x + y ** 3
        max_val = max(r, b, c)
        if max_val == r:
            print("Rafael ganhou")
        elif max_val == b:
            print("Beto ganhou")
        else:
            print("Carlos ganhou")

if __name__ == "__main__":
    max_funcao()