import os
from send2trash import send2trash

# os.chdir('..')
# print(os.path.exists('/Users/mhirleylopes/Desktop'))
# res = os.path.join(os.getcwd(), 'leitura_de_arquivos')
# os.chdir(res)
# os.mknod("arquivo_teste.txt")
# os.mkdir('dir_teste')
# os.makedirs('dir_teste/dir_test_1/dir_teste_2', exist_ok=True)
# os.rename('teste_dir/dir_test_1', 'teste_dir/teste_dir_1')

# os.rmdir('teste_dir')

# os.makedirs('dir_1/dir_2/dir_3')

# with open('dir_1/dir_2/dir_3/teste_1.txt', 'w') as file:
#     pass

# for file in os.scandir('dir_1/dir_2'):
#     if file.is_file():
#         os.remove(file.path)
#     if not file.is_file():
#         os.rmdir(file.path)
#
# os.chdir('..')
# os.rmdir('testing')

# os.makedirs('teste_1/teste_2/teste_3')
# os.removedirs('teste_1/teste_2/teste_3')

send2trash('texto_x.txt')