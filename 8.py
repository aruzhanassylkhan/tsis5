import re
string = input()

x = r"^[a-z]+_[a-z]+$"
if re.search(x, string):
    print('Not matched')
else:
    print('matched')