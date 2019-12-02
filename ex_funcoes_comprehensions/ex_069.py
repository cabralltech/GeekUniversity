import fracao

# Programa Principal
fra1_num = int(input('Numerador 1ª fração: '))
fra1_den = int(input('Denominador 1ª fração: '))
fra2_num = int(input('Numerador 2ª fração: '))
fra2_den = int(input('Denominador 2ª fração: '))
p = f'{fra1_num}/{fra1_den}'
q = f'{fra2_num}/{fra2_den}'
print(f'p = {p}\nq = {q}')
print('- ' * 15)
ps = fracao.simples(fra1_num, fra1_den)
qs = fracao.simples(fra2_num, fra2_den)
print(f'{p} simplificado = {fracao.frac(ps)}\n{q} simplificado = {fracao.frac(qs)}')
print('- ' * 15)
print(f'{fracao.frac(ps)} + {fracao.frac(qs)} = {fracao.soma(ps, qs)}')
print(f'{fracao.frac(ps)} - {fracao.frac(qs)} = {fracao.sub(ps, qs)}')
print(f'{fracao.frac(ps)} x {fracao.frac(qs)} = {fracao.mult(ps, qs)}')
print(f'{fracao.frac(ps)} / {fracao.frac(qs)} = {fracao.div(ps, qs)}')
