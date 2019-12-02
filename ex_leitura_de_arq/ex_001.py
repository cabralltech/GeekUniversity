with open('arq.txt', 'a') as file:
    while True:
        ans = input('Digite um caracter: ')
        if 'O' in ans:
            break
        else:
            file.write(ans)
with open('arq.txt', 'r') as file:
    res = file.read()
for i in res:
    print(i)
