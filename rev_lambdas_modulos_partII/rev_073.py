def habi():
    hab = {}
    while True:
        hab['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]
        if hab['sexo'] not in 'MF':
            print('* Favor digitar M ou F *')
        else:
            break
    print('- ' * 5)
    while True:
        hab['olhos'] = input('Cor dos olhos:\n'
                             '[ A ] azuis\n'
                             '[ C ] castanhos\n'
                             'Digite opção: ').upper().strip()[0]
        if hab['olhos'] not in 'AC':
            print('* Favor digitar uma das opções abaixo *')
        else:
            break
    print('- ' * 5)
    while True:
        hab['cabelo'] = input('Cor dos cabelos:\n'
                              '[ L ] louros\n'
                              '[ C ] castanhos\n'
                              '[ P ] pretos\n'
                              'Digite opção: ').strip().upper()[0]
        if hab['cabelo'] not in 'LCP':
            print('* Favor digitar uma das opções abaixo *')
        else:
            break
    print('- ' * 5)
    while True:
        try:
            hab['idade'] = int(input('Idade: '))
            if 0 <= hab['idade'] <= 130:
                break
            else:
                print('* Favor digitar uma idade válida *')
        except ValueError:
            print('* Favor digitar uma idade válida *')
    print('- ' * 10)
    return hab


def med_cas_pre(h):
    soma = sum(
        map(lambda x: x['idade'],
            (filter(lambda y: y['olhos'] == 'C' and y['cabelo'] == 'P', h)))
    )
    qtd = len([a for a in h if a['olhos'] == 'C' and a['cabelo'] == 'P'])
    return round(soma/qtd, 1)


def maior_idade(h):
    return max(x['idade'] for x in h)


def filtro(h):
    return len([x for x in h if 18 <= x['idade'] <= 35 and x['olhos'] == 'A' and x['cabelo'] == 'L'])


# Programa Principal
habs = [habi() for x in range(5)]
print('= ' * 15)
print(f'A média de idade das pessoas de olhos castanhos e cabelo preto é {med_cas_pre(habs)} anos')
print(f'A maior idade entre os habitantes é {maior_idade(habs)} anos')
print(f'Homens louros dos olhos azuis entre 18 e 35 anos: {filtro(habs)} habitantes')
