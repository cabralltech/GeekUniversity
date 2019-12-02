from csv import DictWriter
from validacao import go_on

with open('arquivo_teste.csv', 'a') as file:
    headers = ('Nome', 'Gênero', 'Diretor(a)')
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    while True:
        nome = input('Nome: ').strip().title()
        genero = input('Gênero: ').strip().title()
        diretor = input('Diretor: ').strip().title()
        csv_writer.writerow({
            'Nome': nome,
            'Gênero': genero,
            'Diretor(a)': diretor
        })
        if go_on('filme') == 'N':
            break


