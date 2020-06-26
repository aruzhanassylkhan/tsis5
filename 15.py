import re
string = input()

x = r'^5'

if re.search(x, string):
    print("Yes")
else:
    print("No")