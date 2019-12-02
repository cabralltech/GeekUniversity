with open('contatos.txt', 'a') as agenda:
    while True:
        nome = input('Nome completo: ').title()
        fone = input(f'Telefone: ')
        try:
            if int(fone) == 0:
                break
        except ValueError:
            agenda.write(f'{nome:<20}')
            agenda.write(f'{fone}\n')
