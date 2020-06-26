import re
text = str(input())

x = re.findall(r"\b\w{3,5}\b", text)
print(x)