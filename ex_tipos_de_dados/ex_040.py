enca = 30.0
dias = int(input('Dias trabalhados: '))
bruto = enca * dias
liquido = bruto - (bruto * (8 / 100))
print(f'Pagamento para encanador com desconto de IR: R$ {liquido:.2f}')
