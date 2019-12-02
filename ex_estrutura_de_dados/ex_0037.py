from random import randint
num = []
for i in range(11):
    n = randint(1, 20)
    if len(num) < 6:
        if i == 0 or n > num[-1]:
            num.append(n)
        else:
            pos = 0
            while pos < len(num):
                if n <= num[pos]:
                    num.insert(pos, n)
                    break
                pos += 1
    else:
        if i == 6 or n < num[-1]:
            num.append(n)
        else:
            p = 6
            while p < len(num):
                if n >= num[p]:
                    num.insert(p, n)
                    break
                p += 1
print(num)
