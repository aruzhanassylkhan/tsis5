import re

text = str(input())
for i in text:
    print(re.sub(r" ?\([^)]+\)", "", text))