import re
text = str(input())
x = re.findall(r"\b\w{4,}\b", text)

print(x)