import re
string = input()

x = r'\Bz\B'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')