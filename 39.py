import re
text = str(input())
x = re.sub(' +',' ',text)

print(x)