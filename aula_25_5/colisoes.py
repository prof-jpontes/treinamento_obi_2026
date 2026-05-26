x0A, y0A, x1A, y1A = map(int, input().split())
x0B, y0B, x1B, y1B = map(int, input().split())

saida = 1
if (x1B < x0A) or (x0B > x1A) or (y0A > y1B) or (y0B > y1A):
    saida = 0
    
print(saida)