text = input()
new_text = ""

for i in text:
    if i == " ":
        new_text += "_"
    elif i == "_":
        new_text += " "
    else:
        new_text += i

print(new_text)