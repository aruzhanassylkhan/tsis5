import re
string = input()

x = 'ab*?'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')

