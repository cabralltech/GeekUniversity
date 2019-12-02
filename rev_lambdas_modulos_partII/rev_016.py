def desenha_linha(vl, smb):
    return smb * vl


while True:
    try:
        valor = int(input('Valor: '))
        break
    except ValueError:
        print('Valor inválido')
while True:
    try:
        simbolo = input('Símbolo: ')
        break
    except:
        print('Símbolo não reconhecido')
print(desenha_linha(valor, simbolo))
