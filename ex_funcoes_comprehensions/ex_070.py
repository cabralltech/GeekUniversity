import rac


p = int(input('Numerador: '))
q = int(input('Denominador: '))
print(f'Número racional: {rac.frac(p,q)}')
print('- ' * 15)
x = []
for i in range(2):
    x.append(int(input('Valor: ')))
print(f'Negativo de {rac.frac(x[0], x[1])} = {rac.neg(x)}')
print('- ' * 15)
y = []
for c in range(2):
    y.append(int(input('Valor: ')))
xf = rac.frac(x[0], x[1])
yf = rac.frac(y[0], y[1])
print(f'{xf} + {yf} = {rac.soma(x, y)}')
print(f'{xf} x {yf} =  {rac.mult(x, y)}')
print(f'{xf} / {yf} = {rac.divide(x, y)}')
