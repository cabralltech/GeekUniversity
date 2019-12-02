soma = 0
inicio = int(input('Inicio do intervalo: '))
fim = int(input('Fim do intervalo: '))
if inicio > fim:
    print('ERRO! Valores de início e fim inválidos')
else:
    for i in range(inicio, fim+1):
        if i % 2 != 0:
            soma += i
    print(f'A soma dos valores ímpares é {soma}')
