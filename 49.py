import re
text = str(input())

x = re.compile(r'\W*\b\w{1,3}\b')
print(x.sub('',text))