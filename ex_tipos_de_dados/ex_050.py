from datetime import datetime
atual = datetime.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Você nasceu em {ano} e completa {idade} neste ano de {atual}')