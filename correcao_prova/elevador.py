N = int(input())

segundos = 0

predio = list(map(int, input().split()))

for i in range(1, N):
    segundos += abs(predio[i] - predio[i-1])
print(segundos)
