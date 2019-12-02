vetor = []
c = n = 0
while c < 100:
    n += 1
    if n % 7 == 0 or n // 1 % 10 == 7:
        vetor.append(n)
        c += 1
print(vetor)
print('- ' * 15)

# vetor2 = [n for n in range(20) if n % 7 == 0 or n // 1 % 10 == 7]  doesn't quite work
# vetor2 = list(filter(lambda n: n % 7 == 0 or n // 1 % 10 == 7, range(20))) doesn't quite work either
# print(vetor2)
# we need a counter to control
