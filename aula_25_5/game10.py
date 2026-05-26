N = int(input())
D = int(input())
A = int(input())

saida = D - A

if saida < 0:
    saida = N - A + D

print(saida)

# if A <= D: 
#     print(D - A)
# else: 
#     print(N - A + D)