import re
string = input()

found = re.search('[^a-zA-Z0-9.]', string)
print(found)

