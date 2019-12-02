semana = ('segunda-feira', 'terça-feira', 'quarta-feira',
          'quinta-feira', 'sexta-feira', 'sábado', 'domingo')
num = int(input('Digite um valor de 1 a 7 para ver o dia da semana: '))
print(f'O dia da semana é {semana[num-1].upper()}')

mes = ('janeiro', 'fevereiro', 'março', 'abril', 'maio',
       'junho', 'julho', 'agosto', 'setembro', 'outubro',
       'novembro', 'dezembro')
num = int(input('Digite um valor de 1 a 12 para ver o mês: '))
print(f'O mês digitado é {mes[num-1].upper()}')
