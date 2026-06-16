# OBI2026 Prog. Nvel 2 Fase 1
# Torre de Número

N = int(input())

torre = []
X = N

#X in torre ( V ou F)

while not (X in torre):
    print(X)
    torre.append(X)

    milhar = X // 1000
    X = X % 1000
    centena = X // 100
    X = X % 100
    dezena = X // 10
    X = X % 10
    unidade = X

    # Encontrar o maior, o segundo maior, o terceiro maior e o menor número

    min_U_D = min(unidade, dezena)
    min_C_M = min(centena, milhar)
    A = min(min_U_D, min_C_M) # O menor

    max_U_D = max(unidade, dezena)
    max_C_M = max(centena, milhar)
    D = max(max_C_M, max_U_D) # O maior
    
    aux1 = max(min_U_D, min_C_M)
    aux2 = min(max_U_D, max_C_M)
    B = min(aux1, aux2) # O segundo menor

    C = max(aux1, aux2) # O segundo maior

    X1 = A * 1000 + B * 100 + C * 10 + D
    X2 = D * 1000 + C * 100 + B * 10 + A

    X = X2 - X1