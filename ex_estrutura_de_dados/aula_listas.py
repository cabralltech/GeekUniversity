nome = 'Mhirley Lopes'
nome = nome.split('-')
print(nome)
nome = ' '.join(nome)
print(nome)

""" 
carrinho = []
produto = ' '
while produto != 'sair':
    produto = input("Adicione produto ao carrinho, ou digite 'sair': ")
    if produto != 'sair':
        carrinho.append(produto)
print(carrinho)
"""
nome = ['Gustavo', 'José', 'dos', 'Santos']
nome1, nome2, nome3, nome4 = nome
print(f'{nome1}\n{nome2}\n{nome3}\n{nome4}')
