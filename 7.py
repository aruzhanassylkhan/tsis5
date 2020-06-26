import re
string = input()

x = r'^[a-z]+_[a-z]+$'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')