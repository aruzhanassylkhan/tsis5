import re
text = str(input())
x = re.sub('Road$', 'Rd.', text)

print(x)