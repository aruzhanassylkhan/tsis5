import re
string = input()

x = r'ab{2,3}?'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')