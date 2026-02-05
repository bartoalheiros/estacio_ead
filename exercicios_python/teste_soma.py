import unittest

class TesteInicio(unittest.TestCase):

    def test_soma_igual(self):
        numeros = [5, 10, 20]
        self.assertEqual(35,sum(numeros))

    def test_soma_diferente(self):
        numeros = [5, 10, 20]
        self.assertNotEqual(35,sum(numeros))