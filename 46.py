import re
text = input()
for i in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (i.start(), i.end(), i.group(0)))