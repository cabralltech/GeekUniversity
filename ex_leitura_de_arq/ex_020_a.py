nomes = []
notas = []
while True:
    nomes.append(input('Nome: ').title().strip())
    notas.append(float(input('Nota final: ').replace(',', '.')))
    while True:
        ans = input('Quer cadastrar outrx alunx? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            break
    if ans == 'N':
        break
with open('notas_alunxs_2.txt', 'w') as nota:
    nota.write(f'{"NOME":<40}{"NOTA FINAL"}\n')
    for i in range(len(notas)):
        nota.write(f'{nomes[i]:<40}{notas[i]} \n')

