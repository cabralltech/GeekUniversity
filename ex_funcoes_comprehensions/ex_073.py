def dados():
    pessoa = {}
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    pessoa['cabelo'] = input('Cor dos cabelos:\n'
                             '[ L ] louros\n'
                             '[ P ] pretos\n'
                             '[ C ] castanhos\n'
                             'Digite a opção: ').strip().upper()[0]
    pessoa['olhos'] = input('Cor dos olhos:\n'
                            '[ A ] azuis\n'
                            '[ C ] castanhos\n'
                            'Digite a opção: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    return pessoa


def media_idade(lis):
    lista = []
    for x in lis:
        if x['cabelo'] == 'C' or x['cabelo'] == 'P':
            lista.append(x['idade'])
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)
    return media


def maior(li):
    l = []
    for p in li:
        l.append(p['idade'])
    ma = 0
    for c in range(len(l)):
        if c == 0:
            ma = l[c]
        else:
            if l[c] > ma:
                ma = l[c]
    return ma


def mul_18_35(pes):
    cont = 0
    for pe in pes:
        if pe['sexo'] == 'F' and 18 <= pe['idade'] <= 35 and pe['cabelo'] == 'L' and pe['olhos'] == 'A':
            cont += 1
    return cont


# Programa Principal
cadastro = []
for i in range(5):
    print('- ' * 5)
    cadastro.append(dados())
print('- ' * 15)
print(f'A média da idade de pessoas de cabelos pretos e castanhos é {media_idade(cadastro):.1f}')
print(f'A maior idade cadastrada é {maior(cadastro)}')
print(f'Foram cadastradas {mul_18_35(cadastro)} mulheres entre 18 e 35 anos, loiras de olhos azuis')
