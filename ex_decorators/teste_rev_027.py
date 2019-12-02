import unittest
from rev_027 import Alunx, Turma


class AlunxTeste(unittest.TestCase):
    def setUp(self):
        self.alunx = Alunx(mat=100, nome='Mhirley Lopes', notas=[8.7, 9.8])

    def teste_init(self):
        self.assertEqual(type(self.alunx['mat']), int)
        self.assertGreater(len(self.alunx['nome']), 3)
        self.assertEqual(all(map(lambda a: type(a) == float, self.alunx['notas'])), True)

    def teste_media(self):
        self.assertEqual(self.alunx.media(), 9.2)


class TurmaTeste(unittest.TestCase):
    def setUp(self):
        self.turma = Turma(num=2, disc='Matemática', prof='Mhirley Lopes')

    def teste_init(self):
        self.assertEqual(type(self.turma.num), int)
        self.assertEqual(type(self.turma.disc), str)
        self.assertGreater(len(self.turma.prof), 3)


if __name__ == '__main__':
    unittest.main()
