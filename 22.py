import re

text = input()
pattern = input()

for i in re.finditer(pattern, text):
    a = i.start()
    b = i.end()
    print(text[a:b], a, b)