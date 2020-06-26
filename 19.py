import re
words = [ 'fox', 'dog', 'horse' ]

text = 'The quick brown fox jumps over the lazy dog.'
for i in words:
    print((i),)
    if re.search(i,  text):
        print('Matched!')
    else:
        print('Not Matched!')