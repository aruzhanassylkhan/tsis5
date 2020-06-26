import re
text = str(input()) 

x = re.sub('[a-z]', '', text)

print(x)