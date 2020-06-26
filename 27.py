import re

text = str(input())
x = re.split(r"\D+", text)

for i in x:
    print(i)