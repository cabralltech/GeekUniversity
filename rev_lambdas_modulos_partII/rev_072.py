def soma(v1, v2, vpont):
    xr = (v1[0] + v2[0]) + vpont[0]
    yr = (v1[1] + v2[1]) + vpont[1]
    zr = (v1[2] + v2[2]) + vpont[2]
    vr = xr, yr, zr
    return vr


while True:
    try:
        x1 = int(input('"x" para vetor 1: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y1 = int(input('"y" para vetor 1: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        z1 = int(input('"z" para vetor 1: '))
        break
    except ValueError:
        print('\033[mERRO! Valor inválido\033[m')
vet1 = x1, y1, z1
print('- ' * 15)
while True:
    try:
        x2 = int(input('"x" para vetr 2: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y2 = int(input('"y" para vertor 2: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        z2 = int(input('"z" para vetor 2: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
vet2 = x2, y2, z2
print('- ' * 15)
while True:
    try:
        x = int(input('"x" ponteiro: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y = int(input('"y" ponteiro: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        z = int(input('"z" ponteiro: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
vetp = x, y, z
print('- ' * 15)
print(soma(vet1, vet2, vetp))
