import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_tilavuus_saldo_neg(self):
        varasto2 = Varasto(-10, -10)
        self.assertEqual(varasto2.tilavuus, 0)
        self.assertEqual(varasto2.saldo, 0)

    def test_konstruktori_saldo_suurempi(self):
        varasto2 = Varasto(5, 10)
        self.assertEqual(varasto2.saldo, 5)

    def test_lisaa_varastoon_neg(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        saldo_jalkeen = self.varasto.saldo
        self.assertEqual(saldo_ennen, saldo_jalkeen)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_neg(self):
        result = self.varasto.ota_varastosta(-10)
        self.assertEqual(result, 0.0)

    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(10)
        self.assertEqual(maara, 5)

    def test_output(self):
        output = self.varasto.__str__()
        self.assertEqual(output, "saldo = 0, vielä tilaa 10")