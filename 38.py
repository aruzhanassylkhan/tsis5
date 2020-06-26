import re
text = str(input())
x = re.findall(r'"(.*?)"', text)

print(x)