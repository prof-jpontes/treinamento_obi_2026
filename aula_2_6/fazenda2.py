N = 1

massa = int(input()) #primeiro boi
maisLeve = massa
maisPesado = massa
soma = massa

while True:
    massa = int(input())
    
    if massa <= 0: break

    soma += massa

    if massa > maisPesado:
        maisPesado = massa

    if massa <  maisLeve:
        maisLeve = massa
    N += 1

media = soma/N

print(maisLeve, maisPesado, media)


