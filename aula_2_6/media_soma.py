soma = 0
q = 0
while True:
    n = int(input())

    if n < 0:
        break

    soma += n
    q += 1

print("Soma:", soma)
print("Média", soma/q)