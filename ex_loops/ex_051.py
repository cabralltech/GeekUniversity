from datetime import date
salario = 2000
aumento = 0.015
atual = date.today().year
salario += salario * aumento
aumento *= 2
ano = 1997
while ano <= atual:
    salario += salario * aumento
    ano += 1
print(f'Atualmente o funicionário recebe R${salario:.2f}')
