e2s = []
e3s = []
fat = 0
for i in range(20, 0, -1):
    num = i
    if i % 2 == 0:
        e2 = 0
        while num % 2 == 0:
            num /= 2
            e2 += 1
        e2s.append(e2)
    elif i % 3 == 0:
        e3 = 0
        while num % 3 == 0:
            num /= 3
            e3 += 1
        e3s.append(e3)
fat = (2 ** max(e2s)) * (3 ** max(e3s)) * 5 * 7 * 11 * 13 * 17 * 19
print(fat)
