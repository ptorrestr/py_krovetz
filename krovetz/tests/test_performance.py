import krovetz
import pytest

def stem_many(ks, word):
  return ks.stem(word)

@pytest.mark.parametrize('word', ['word', 'running', 'walked', 'users', 'element', 'happier'])
def test_stem(benchmark, word):
  ks = krovetz.PyKrovetzStemmer()
  result = benchmark(stem_many, ks, word)
