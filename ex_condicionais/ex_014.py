trab_lab = float(input('Trabalho de Laboratório: '))
ava_sem = float(input('Avaliação semestral: '))
exa_fin = float(input('Exame final: '))
media = ((trab_lab * 2) + (ava_sem * 3) + (exa_fin * 5)) / 10
if 0 <= media < 3:
    print('REPROVADO')
elif 3 <= media < 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
