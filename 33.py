import re
text = str(input())

x = re.findall(r"\b\w{5}\b", text)
print(x)