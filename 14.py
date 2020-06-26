import re
string = input()

x = r'^[a-zA-Z0-9_]*$'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')