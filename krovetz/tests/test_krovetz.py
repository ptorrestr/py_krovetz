import unittest
import krovetz

class TestKrovetz(unittest.TestCase):
  def test_do_simple_stem(self):
    ks = krovetz.PyKrovetzStemmer()
    self.assertEqual(ks.kstem_stemmer("walked"), "walk")
    self.assertEqual(ks.kstem_stemmer("run"), "run")
