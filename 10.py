import re
string = input()

x = r'^\w+'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')