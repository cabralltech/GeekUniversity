with open("aula_de_escrita.txt", "w") as file:
    while True:
        fruta = input('Informe uma fruta ou digite "sair": ')
        if fruta != "sair":
            file.write(f'{fruta}\n')
        else:
            break

