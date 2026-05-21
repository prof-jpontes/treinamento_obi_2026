j1 = input()
j2 = input()
j3 = input()
j4 = input()
j5 = input()
j6 = input()

ttlV = 0

if j1 == "V": ttlV += 1
if j2 == "V": ttlV += 1
if j3 == "V": ttlV += 1
if j4 == "V": ttlV += 1
if j5 == "V": ttlV += 1
if j6 == "V": ttlV += 1

if ttlV >= 5: print(1)
elif ttlV >= 3: print(2)
elif ttlV >= 1: print(3)
else: print(-1)