import os

# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# print(os.path.isabs('PycharmProjects/GeekUniversity'))

# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# res = os.path.join(os.getcwd(), 'leitura_de_arquivos')
# os.chdir(res)
# print(os.getcwd())

# os.chdir('/Users/mhirleylopes')
# print(os.getcwd())
# for i in os.listdir():
#     print(i)
# for x in os.listdir('/Users/mhirleylopes/Desktop/Parler'):
#     print(x)
arquivos = list(os.scandir())
print(arquivos[0].inode())
print(arquivos[1].stat())
print(dir(arquivos))
os.scandir().close()

