import os

"""
os.chdir('/Users/mhirleylopes/Desktop/MHIRLEY')
for i in os.listdir('/Users/mhirleylopes/Desktop/MHIRLEY'):
    if i == 'OPT-UFSC':
        file = i
for x in os.scandir(os.path.join(os.getcwd(), file)):
    if x.is_file():
        if x.name == 'oficina_mimo_dez_horas.docx':
            arquivo = x.name
os.chdir(os.path.join(os.getcwd(), file))
with open(os.path.join(os.getcwd(), arquivo), ) as arq:
    res = arq.readlines()
res_2 = sum(len(x.split('.')) for x in res)
print(f'O arquivo tem {res_2} linhas')
"""

# os.chdir('..')

# with open('leitura_de_arquivos/aula_de_escrita.txt') as file:
#     res = file.readlines()
# print(f'O arquivo tem {len(res)} linhas')


while True:
    file = input('Digite o path absoluto de um arquivo: ')
    try:
        with open(file) as f:
            answer = f.readlines()
            break
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m Tente novamente')
print('- ' * 15)
print(f'O arquivo contem {len(answer)} linhas')
