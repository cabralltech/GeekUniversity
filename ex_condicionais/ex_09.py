salario = float(input('Salário: '))
parcela = float(input('Parcela empréstimo: '))
if parcela > (salario * 0.20):
    print('EMPRÉSTIMO NÃO CONCEDIDO')
else:
    print('EMPRÉSTIMO CONCEDIDO')
