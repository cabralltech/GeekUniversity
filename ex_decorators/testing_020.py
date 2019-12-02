import unittest
from rev_020 import Turma


class TurmaTest(unittest.TestCase):
    def setUp(self):
        self.mat = Turma()
        self.mat.nomes = ['Mhirley Lopes']
        self.mat.notas = [9.0]

    def testing_init(self):
        self.assertEqual(type(self.mat.num), int)
        self.assertEqual(type(self.mat.nomes), list)
        self.assertEqual(type(self.mat.notas), list)

    def testing_nom(self):
        # self.assertEqual(type(self.mat.nom()), str)
        self.assertEqual(self.mat.nom(), 'Mhirley Lopes')

    def testing_nota(self):
        # self.assertEqual(type(self.mat.nota()), float)
        self.assertEqual(self.mat.nota(), 9.0)


if __name__ == '__main__':
    unittest.main()
