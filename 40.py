import re

text = str(input())
x = re.sub(r'\s+', '',text)

print(x)