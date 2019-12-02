preco = float(input('Preço do produto: R$ '))
desc = preco - (preco * (12 / 100))
print(f'O preço final com 12% de desconto é R$ {desc:.2f}')

salario = float(input('Salário: R$ '))
acres = salario + (salario * (25 / 100))
print(f'O salário com 25% de aumento é R$ {acres:.2f}')
