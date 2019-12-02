def maiscula(char):
    return char.upper()


while True:
    carac = input('Digite um caractere: ')
    if not carac or len(carac) > 1 or carac.isnumeric():
        print('\033[31mERRO! Favor, digitar UM caractere\033[m')
    else:
        break
print(maiscula(carac))
