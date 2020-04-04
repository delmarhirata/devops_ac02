from unittest import TestCase
from com.delmar.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([11, 2]), 13, "Deveria ser 13")