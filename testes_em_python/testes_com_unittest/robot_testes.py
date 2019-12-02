import unittest
from robot import Robot


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.mega_man = Robot('Mega-Man', bateria=50)

    def test_carregar(self):
        self.assertEqual(self.mega_man.carregar(), 100)

    def test_dizer_nome(self):
        if self.mega_man.bateria > 10:
            self.assertEqual(self.mega_man.dizer_nome(), 'BEEP BOOP - Meu nome é Mega-Man')
        else:
            self.assertLess(self.mega_man.dizer_nome(), 'Bateria insuficiente, recarregue a bateria')

    def test_aprender_habilidades(self):
        self.assertEqual(self.mega_man.aprender_habilidades(
            nova_habilidade='lutar Kung-Fu', custo=85
        ), 'Bateria insuficiente, recarregue a bateria')
        self.assertEqual(self.mega_man.aprender_habilidades(
            nova_habilidade='nadar', custo=30
        ), 'Mega-man sabe nadar agora')

    def tearDown(self):
        return None

if __name__ == '__main__':
    unittest.main()
