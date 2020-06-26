import re

pattern = 'exercises'
text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'
x = re.findall(pattern, text)
print(x)