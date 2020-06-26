import re

text = str(input())

x = re.findall(r"[ae]\w+", text)

print(x)