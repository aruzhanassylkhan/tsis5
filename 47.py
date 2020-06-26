import re
text = str(input())

print(re.split(r'; |, |\*|\n', text))