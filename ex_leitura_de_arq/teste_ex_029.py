import unittest
from ex_029 import Vendedor, Vendas


class VendedorTests(unittest.TestCase):
    def setUp(self):
        self.vend = Vendedor()

    def test_init(self):
        self.assertEqual(self.vend['codigo'], 100)
        self.assertEqual(self.vend['nome'], 'Mhirley Lopes')
        self.assertEqual(type(self.vend["vendas"]), list)


class VendasTests(unittest.TestCase):
    def setUp(self):
        self.venda = Vendas()

    def test_printar(self):
        pass







if __name__ == '__main__':
    unittest.main()