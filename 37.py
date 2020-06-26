import re

text = str(input())

print(''.join(x.capitalize() or '_' for x in text.split('_')))