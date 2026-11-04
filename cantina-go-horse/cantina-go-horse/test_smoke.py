"""Teste de fumaça (go-horse tem pouca rede de proteção). python -m unittest"""
import unittest
import cantina_go_horse as c


class Smoke(unittest.TestCase):
    def setUp(self):
        c.fila.clear()

    def test_pix_com_combo(self):
        self.assertEqual(c.processa_pedido("Ana", ["coxinha", "suco"], "pix", {"chave": "x"}), 1)
        self.assertEqual(c.fila[0]["total"], 9)

    def test_cartao_recusado_nao_entra_na_fila(self):
        self.assertIsNone(c.processa_pedido("Caio", ["coxinha"], "cartao", {"limite": 1}))
        self.assertEqual(len(c.fila), 0)

    def test_item_invalido(self):
        self.assertIsNone(c.processa_pedido("Gabi", ["pizza"], "pix", {"chave": "x"}))


if __name__ == "__main__":
    unittest.main()
