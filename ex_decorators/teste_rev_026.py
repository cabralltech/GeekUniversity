import unittest
from rev_026 import Alunx, entrada


# class Teste_entrada(unittest.TestCase):
#     def teste_entrada(self):
#         self.assertEqual(entrada(), Alunx(mat=100, sobrenome='Lopes', ano_nasc=1979))


class TesteAlunx(unittest.TestCase):
    def setUp(self):
        self.alunx = Alunx(mat=100, sobrenome='Lopes', ano_nasc=1979)

    def test_init(self):
        self.assertEqual(type(self.alunx['mat']), int)
        self.assertGreater(len(self.alunx["sobrenome"]), 3)
        self.assertEqual(type(self.alunx['ano_nasc']), int)


if __name__ == '__main__':
    unittest.main()
