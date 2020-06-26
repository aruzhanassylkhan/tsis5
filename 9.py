import re
string = input()

x = r'a.*?b$'
if re.search(x, string):
    print('matched')
else:
    print('Not matched')