# OBI2026 Prog. Nvel 1 Fase 1
# Mercadinho

N = int(input()) # Número de pessoas na fila

idades = list(map(int, input().split()))
#idades = [15, 50, 61, 32, 75, 67]

# idosos = 0
# movimentos = 0

# for i in range(N):
#     if(idades[i] >= 60):
#         movimentos = max(movimentos, i - idosos)
#         idosos += 1

# print(movimentos)

# OU

iI = 0
qI = 0
for i in range(N):
    if idades[i] >= 60:
        qI += 1
        iI = i
print(iI - max(qI-1, 0))