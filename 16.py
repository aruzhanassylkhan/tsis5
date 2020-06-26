import re
string = input()

x = re.sub(r'\.[0]*', '.', string)
print(x)