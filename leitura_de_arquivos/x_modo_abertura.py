try:
    with open("texte_x.txt", "x") as file:
        file.write("Eu sou um novo arquivo pra teste\n ")
except FileExistsError:
    print('Arquivo já existente')