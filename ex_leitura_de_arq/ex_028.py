with open('arq_entrada.txt', 'w') as arq:
    arq.write('Este é um arquivo de entrada\n')
    arq.write('Para escrever algo e ter o arquivo\n')
    arq.write('Para poder fazer o exercício completo')
with open('arq_entrada.txt') as a:
    texto = a.readlines()
    with open('arq_saida.txt', 'w') as sa:
        for i in range(len(texto) - 1, -1, -1):
            linha = texto[i].replace('\n', '')
            sa.write(f'{linha[::-1].capitalize()}\n')

