a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
if a < b + c and b < c + a and c < b + a:
    if a != b and c != a and b != c:
        print('Você construiu um triângulo ESCALENO')
    elif a == b == c:
        print('Você construiu um triângulo EQUILÁTERO')
    else:
        print('Você construiu um triângulo ISÓCELES')
else:
    print('Não dá pra fazer um triângulo com essas medidas')
