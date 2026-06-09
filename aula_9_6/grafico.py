N = int(input())

brinquedos = list(map(int, input().split()))

H = max(brinquedos)

for i in range(H, 0, -1):
    for j in range(N):
        if(brinquedos[j] >= i): print(1, end="")
        else: print(0, end="")

        if j != N-1: print(end=" ")
    print()
