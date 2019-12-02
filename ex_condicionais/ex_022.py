idade = int(input('Idade: '))
tempo = int(input('Tempo de serviço: '))
if idade > 60 and tempo > 25:
    print('Pode se aposentar')
elif tempo > 30 or idade > 65:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
