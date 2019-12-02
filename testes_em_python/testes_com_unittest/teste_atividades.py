import unittest
from atividades import comer, dormir


class AtividadesTeste(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(comer(
            comida='quiabo', saudavel=True
        ), 'Eu como quiabo porque gosto de uma vida saudável')
        self.assertEqual(comer(
            comida='pizza', saudavel=False
        ), 'Eu como pizza porque gosto de viver intensamente')

    def test_dormir(self):
        self.assertGreaterEqual(dormir.__defaults__[0], 8,
                                'Eu durmo nove horas por noite e me sinto bem por isso')
        self.assertLess(dormir.__defaults__[0], 8,
                        'Eu durmo três horas por noite e me sinto cansada o tempo inteiro')


if __name__ == '__main__':
    unittest.main()
