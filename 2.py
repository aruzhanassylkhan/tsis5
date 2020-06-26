import re
string = input()

x = 'rab*?'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')

