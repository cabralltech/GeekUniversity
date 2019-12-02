n = input('Nome do arquivo: ')
nome = n + '.txt'
# with open(nome, 'x'):
#     pass
# with open(nome, 'r+') as pop:
#     while True:
#         cid = input('Cidade: ').strip().title()
#         while True:
#             try:
#                 hab = int(input('Habitantes: '))
#                 break
#             except ValueError:
#                 print('\033[31mValor inválido\033[m')
#         pop.write(f'{cid:<40}{hab} mil\n')
#         while True:
#             ans = input('Registrar outra cidade? ').upper().strip()[0]
#             if ans not in 'SN':
#                 print('\033[31mResposta inválida\033[m')
#             else:
#                 break
#         if ans == 'N':
#             break
#     for i in pop:
#         print(i)
with open(nome) as f:
    file = f.readlines()
cidades = (x.split(' ') for x in file)
maior = max(([z for z in y if z.isnumeric()] for y in cidades))[0]
mcid = [a for a in file if maior in a]
with open('nova_populacao.txt', 'w') as np:
    np.write(mcid[0])


