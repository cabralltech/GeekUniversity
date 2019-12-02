alt_degrau = float(input('Qual a altura do degrau (em metros): '))
alt_desejada = float(input('Qual altura vc quer alcançar (em metros)? '))
num_degraus = alt_desejada / alt_degrau
print(f'Você deve subir {int(num_degraus)} para alcançar {alt_desejada:.1f}m de altura')
