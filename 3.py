import re
string = input()

x = r'ab+?'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')