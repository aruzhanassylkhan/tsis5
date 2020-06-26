import re
text =str(input())

redata = re.compile(re.escape('php'), re.IGNORECASE)
#new_text = redata.sub('php', 'PHP Exercises')

print("New Text: ",new_text)  