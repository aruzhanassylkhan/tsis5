import re

string = input()

if re.search(r".*[0-9]$", string):
    print("Yes")
else:
    print("No")
