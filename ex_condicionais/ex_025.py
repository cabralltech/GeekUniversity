print('- ' * 20)
print(f'{"EQUAÇÃO 2º GRAU":^40}')
print('- ' * 20)
a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))
delta = (b ** 2) - (4 * a * c)
raiz = raiz1 = 0
if a == 0:
    print('Isso não é uma equação de segundo grau')
else:
    if delta < 0:
        print('Não existe raiz')
    elif delta == 0:
        raiz = - b / (2 * a)
    elif delta > 0:
        raiz = (- b + (delta ** 0.5)) / (2 * a)
        raiz1 = (- b - (delta ** 0.5)) / (2 * a)
        print(f'As raízes são {raiz:.2f} e {raiz1:.2f}')
