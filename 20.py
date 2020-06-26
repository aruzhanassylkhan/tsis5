import re

word = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'

x = re.search(word, text)
a = x.start()
b = x.end()
print(x.re.pattern, a, b)