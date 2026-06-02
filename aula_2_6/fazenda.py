N = int(input()) #quantidade de bois da fazenda

massa = int(input()) #primeiro boi
maisLeve = massa
maisPesado = massa

soma = massa

for i in range(N-1):
    massa = int(input())
    soma += massa

    if massa > maisPesado:
        maisPesado = massa

    if massa <  maisLeve:
        maisLeve = massa

media = soma/N

print(maisLeve, maisPesado, media)


