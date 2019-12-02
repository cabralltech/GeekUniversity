from csv import writer, reader
from validacao import go_on

# with open('filmes.csv', 'a') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Nome', 'Gênero', 'Diretor'])
#     while True:
#         nome = input('Nome: ').strip().title()
#         genero = input('Gênero: ').strip().title()
#         diretor = input('Diretor(a): ').strip().title()
#         csv_writer.writerow([nome, genero, diretor])
#         if go_on('filme') == 'N':
#             break

with open('filmes.csv') as file:
    csv_reader = reader(file)
    filmes = list(csv_reader)
    filmes.pop()
    with open('filmes.csv', 'w') as f:
        csv_writer = writer(f)
        for filme in filmes:
            csv_writer.writerow(filme)
