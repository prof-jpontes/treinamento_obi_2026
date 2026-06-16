# OBI2026 Prog. Nvel 1 Fase 1
# Receita RevolucionÆria

# Link da prova: https://olimpiada.ic.unicamp.br/static/extras/obi2026/provas/ProvaOBI2026_f1p1.pdf

P = int(input()) # Quantidade de pães
O = int(input()) # Quantidade de ovos

dias_P = P // 2 # Tem pães suficientes para quantos dias?
dias_O = O // 4 # Tem ovos suficientes para quantos dias?

dias = min(dias_P, dias_O)

print(dias)

# OU, RESUMIDAMENTE

#print(min(int(input()) // 2, int(input()) // 4))