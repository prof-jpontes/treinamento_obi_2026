N = int(input())

alvo = 1
marcado = 0

for i in range(N):
    Vi = int(input())
    if Vi == alvo:
        marcado += 1
        alvo = 3 - alvo

print(marcado)