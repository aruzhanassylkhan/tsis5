import re
text = input()
x = re.compile(r"^[0-9]+(\.[0-9]{1,2})?$")
print(x.search(text))


