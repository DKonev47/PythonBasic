import string
text = str(input("Enter text: "))
text = text[:139]
text = text.title()
for i in string.punctuation:
    text = text.replace(i, '')
text = text.replace(" ", "", 140)
one = str('#')
print(one + text)
