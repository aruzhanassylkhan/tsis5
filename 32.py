import re
text = str(input())
x = re.sub("[ ,.]", ":", text, 2)
print(x)