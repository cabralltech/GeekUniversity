from io import StringIO


mensagem = 'Esta é uma mensagem teste\n'

arquivo = StringIO(mensagem)
# arquivo = open("arquivo.txt", "w)
print(arquivo.read())
arquivo.write('Outro texto\n')
arquivo.seek(0)
print(arquivo.read())
