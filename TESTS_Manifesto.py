from manifesto_func import *
import unittest

class DataClean(unittest.TestCase):
    def setUp(self):
        self.f = open("manifesto-data.json")
    def test_roof_text(self):
        roof_text = manifesto_data['Dylan Roof']['Dylan Roof Manifesto']
        self.assertFalse("\n" in roof_text)
        self.assertFalse("\u2026" in roof_text)
        self.assertFalse("\f" in roof_text)
        self.assertFalse("\u2019" in roof_text)
        self.assertFalse("\u201c" in roof_text)
        self.assertFalse("\u201d" in roof_text)
        self.assertFalse("\u2013" in roof_text)
    def test_rodger_text(self):
        rodger_text = manifesto_data['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger']
        self.assertFalse("\n" in rodger_text)
        self.assertFalse("\u2026" in rodger_text)
        self.assertFalse("\f" in rodger_text)
        self.assertFalse("\u2019" in rodger_text)
        self.assertFalse("\u201c" in rodger_text)
        self.assertFalse("\u201d" in rodger_text)
        self.assertFalse("\u2013" in rodger_text)
    def test_cho_text(self):
        cho_text = manifesto_data['Seung Hui Cho']['Seung Hui Cho Manifesto']
        self.assertFalse("\n" in cho_text)
        self.assertFalse("\u2026" in cho_text)
        self.assertFalse("\f" in cho_text)
        self.assertFalse("\u2019" in cho_text)
        self.assertFalse("\u201c" in cho_text)
        self.assertFalse("\u201d" in cho_text)
        self.assertFalse("\u2013" in cho_text)
    def test_auvinen_text(self):
        auvinen_text = manifesto_data['Eric Auvinen']["Natural Selector's Manifesto"]
        self.assertFalse("\n" in auvinen_text)
        self.assertFalse("\u2026" in auvinen_text)
        self.assertFalse("\f" in auvinen_text)
        self.assertFalse("\u2019" in auvinen_text)
        self.assertFalse("\u201c" in auvinen_text)
        self.assertFalse("\u201d" in auvinen_text)
        self.assertFalse("\u2013" in auvinen_text)
    def test_kaczynski_text(self):
        kaczynski_text = manifesto_data['Ted Kaczynski']["Industrial Society and Its Future"]
        self.assertFalse("\n" in kaczynski_text)
        self.assertFalse("\u2026" in kaczynski_text)
        self.assertFalse("\f" in kaczynski_text)
        self.assertFalse("\u2019" in kaczynski_text)
        self.assertFalse("\u201c" in kaczynski_text)
        self.assertFalse("\u201d" in kaczynski_text)
        self.assertFalse("\u2013" in kaczynski_text)
    def test_dorner_text(self):
        dorner_text = manifesto_data['Christopher Dorner']["Christopher Dorner's Manifesto"]
        self.assertFalse("\n" in dorner_text)
        self.assertFalse("\u2026" in dorner_text)
        self.assertFalse("\f" in dorner_text)
        self.assertFalse("\u2019" in dorner_text)
        self.assertFalse("\u201c" in dorner_text)
        self.assertFalse("\u201d" in dorner_text)
        self.assertFalse("\u2013" in dorner_text)
    def test_adkission_text(self):
        adkission_text = manifesto_data['Adkission Manifesto']["The Adkission Manifesto"]
        self.assertFalse("\n" in adkission_text)
        self.assertFalse("\u2026" in adkission_text)
        self.assertFalse("\f" in adkission_text)
        self.assertFalse("\u2019" in adkission_text)
        self.assertFalse("\u201c" in adkission_text)
        self.assertFalse("\u201d" in adkission_text)
        self.assertFalse("\u2013" in adkission_text)
    def tearDown(self):
        self.f.close()
if __name__  == "__main__":
    unittest.main(verbosity=2)
