import re

x = r"([0-9]{1,3})"
results = re.finditer(x, "Exercises number 1, 12, 13, and 345 are important")

for i in results:
    print(i.group(0))