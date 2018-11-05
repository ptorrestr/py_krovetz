import unittest
import krovetz

class TestKrovetz(unittest.TestCase):
  def test_do_simple_stem(self):
    ks = krovetz.PyKrovetzStemmer()
    self.assertEqual(ks.stem("walked"), "walk")
    self.assertEqual(ks.stem("run"), "run")
