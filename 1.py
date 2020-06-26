import re
string = input()

found = re.search(r"[^a-zA-Z0-9.]", string)
print(found)

