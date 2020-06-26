import re
text = str(input())

x = re.compile(r"[\W_]+")
print(x.sub('', text))