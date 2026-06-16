# OBI2026 Prog. Nvel 1 Fase 1
# Encontro de Amigas

A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())

inicio = max(A1, B1, C1)
fim = min(A2, B2, C2)

# if(fim - inicio >= 0): print(fim - inicio + 1)
# else: print(0)

#OU, DE FORMA MELHORADA
print(max(0, fim - inicio + 1))