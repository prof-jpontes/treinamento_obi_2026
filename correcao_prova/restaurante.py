# OBI2026 Prog. Nvel 2 Fase 1
# Restaurante

G1, G2, G3, G4 = map(int, input().split())

mesas = G4 # alocou todos os membros do G4

mesas += G3 # alocou todos os membros do G3
# mesas com G3 têm um lugar vazio

G1 = G1 - G3 #G1 pode se tornar negativo, mas isso não é um problema
# G1, quando negativo, indica a quantidade de mesas que tem G3 e uma cadeira vazia

mesas += G2 // 2
G2 = G2 % 2 # Aqui G2 é 1 ou 0

if G2 == 1:
    mesas += 1
    G1 -= 2

if G1 > 0:
    mesas += (G1 // 4)
    G1 = G1 % 4

if G1 > 0: #aqui eu tenho a garantia de que G1 é menor do que 4
    mesas += 1

print(mesas)