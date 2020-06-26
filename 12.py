import re
string = input()

x = r'\w*z.\w*'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')