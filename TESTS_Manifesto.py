from manifesto_func import *
from class_manifesto import *
import unittest

# Note: Two part test
# Top tests implemented before OOP
# The ones on the bottom are tests for OOP
# Testing based off scraping the data
class DataCapture(unittest.TestCase):
    def setUp(self):
        self.f = open("manifesto-data.json")
    def test_roof_text(self):
        roof_text = manifesto_data['Dylan Roof']['Dylan Roof Manifesto']
        ## assertFalse because the goal is to NOT have it in the text
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
    def test_adkisson_text(self):
        adkisson_text = manifesto_data['Jim Adkisson']["The Adkisson Manifesto"]
        self.assertFalse("\n" in adkisson_text)
        self.assertFalse("\u2026" in adkisson_text)
        self.assertFalse("\f" in adkisson_text)
        self.assertFalse("\u2019" in adkisson_text)
        self.assertFalse("\u201c" in adkisson_text)
        self.assertFalse("\u201d" in adkisson_text)
        self.assertFalse("\u2013" in adkisson_text)
    def tearDown(self):
        self.f.close()

class DataCleaning(unittest.TestCase):
    def test_stopwords(self):
        for stopword in stopwords:
            self.assertFalse(stopword in filtered_adkisson)
            self.assertFalse(stopword in filtered_auvinen)
            self.assertFalse(stopword in filtered_cho)
            self.assertFalse(stopword in filtered_dorner)
            self.assertFalse(stopword in filtered_kaczynski)
            self.assertFalse(stopword in filtered_rodger)
            self.assertFalse(stopword in filtered_roof)
    def test_wordlists_adkisson(self):
        self.assertEqual(type(adkisson_word_lst[0]), type(""))
        self.assertEqual(type(adkisson_word_lst), type([]))
        for word in adkisson_word_lst:
            # https://stackoverflow.com/questions/33205288/python-check-if-a-string-contains-a-digit
            if any(c.isdigit() for c in word): # skips numbers
                pass
            else:
                self.assertTrue(word.islower()) # Check if tokens are lowercase
    def test_wordlists_auvinen(self):
        self.assertEqual(type(auvinen_word_lst[0]), type(""))
        self.assertEqual(type(auvinen_word_lst), type([]))
        for word in auvinen_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())
    def test_wordlists_cho(self):
        self.assertEqual(type(cho_word_lst[0]), type(""))
        self.assertEqual(type(cho_word_lst), type([]))
        for word in cho_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())
    def test_wordlists_dorner(self):
        self.assertEqual(type(dorner_word_lst[0]), type(""))
        self.assertEqual(type(dorner_word_lst), type([]))
        for word in dorner_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())
    def test_wordlists_kaczynski(self):
        self.assertEqual(type(kaczynski_word_lst[0]), type(""))
        self.assertEqual(type(kaczynski_word_lst), type([]))
        for word in kaczynski_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())
    def test_wordlists_rodger(self):
        self.assertEqual(type(rodger_word_lst[0]), type(""))
        self.assertEqual(type(rodger_word_lst), type([]))
        for word in rodger_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())
    def test_wordlists_roof(self):
        self.assertEqual(type(roof_word_lst[0]), type(""))
        self.assertEqual(type(roof_word_lst), type([]))
        for word in roof_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())


# ----------------------------------------------#

## Tests created after implementing OOP ##
class TestManifesto(unittest.TestCase):

    def setUp(self):
        self.dylan_roof = Manifesto("Dylan Roof", "Dylan Roof Manifesto", manifesto_data)

        self.elliot_rodger = Manifesto("Elliot Rodger", "The Twisted World: The Story of Elliot Rodger", manifesto_data)

        self.jim_adkisson = Manifesto("Jim Adkisson", "The Adkisson Manifesto", manifesto_data)

    def test_word_lst(self):
        self.assertEqual(type(self.dylan_roof.word_lst()[0]), type(""))
        self.assertEqual(type(self.dylan_roof.word_lst()), type([]))
        for word in self.dylan_roof.word_lst():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.elliot_rodger.word_lst()[0]), type(""))
        self.assertEqual(type(self.elliot_rodger.word_lst()), type([]))
        for word in self.elliot_rodger.word_lst():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.jim_adkisson.word_lst()[0]), type(""))
        self.assertEqual(type(self.jim_adkisson.word_lst()), type([]))
        for word in self.jim_adkisson.word_lst():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

    def test_unique_words(self):
        self.assertEqual(type(self.dylan_roof.unique_words()[0]), type(""))
        self.assertEqual(type(self.dylan_roof.unique_words()), type([]))
        for word in self.dylan_roof.unique_words():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.elliot_rodger.unique_words()[0]), type(""))
        self.assertEqual(type(self.elliot_rodger.unique_words()), type([]))
        for word in self.elliot_rodger.unique_words():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.jim_adkisson.unique_words()[0]), type(""))
        self.assertEqual(type(self.jim_adkisson.unique_words()), type([]))
        for word in self.jim_adkisson.unique_words():
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

    def test_stopwords2(self):
        for stopword in stopwords:
            self.assertFalse(stopword in self.jim_adkisson.filtered_manifesto)
            self.assertFalse(stopword in self.elliot_rodger.filtered_manifesto)
            self.assertFalse(stopword in self.dylan_roof.filtered_manifesto)

    def test_tokens(self):
        self.assertEqual(type(self.dylan_roof.manifesto_word_lst[0]), type(""))
        self.assertEqual(type(self.dylan_roof.manifesto_word_lst), type([]))
        for word in self.dylan_roof.manifesto_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.elliot_rodger.manifesto_word_lst[0]), type(""))
        self.assertEqual(type(self.elliot_rodger.manifesto_word_lst), type([]))
        for word in self.elliot_rodger.manifesto_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

        self.assertEqual(type(self.jim_adkisson.manifesto_word_lst[0]), type(""))
        self.assertEqual(type(self.jim_adkisson.manifesto_word_lst), type([]))
        for word in self.jim_adkisson.manifesto_word_lst:
            if any(c.isdigit() for c in word):
                pass
            else:
                self.assertTrue(word.islower())

    def test_manifesto_dict(self):
        self.assertEqual(type(self.jim_adkisson.manifesto), type(""))
        self.assertEqual(self.jim_adkisson.author, "Jim Adkisson")

        self.assertEqual(type(self.dylan_roof.manifesto), type(""))
        self.assertEqual(self.dylan_roof.author, "Dylan Roof")

        self.assertEqual(type(self.elliot_rodger.manifesto), type(""))
        self.assertEqual(self.elliot_rodger.author, "Elliot Rodger")




if __name__  == "__main__":
    unittest.main(verbosity=2)
