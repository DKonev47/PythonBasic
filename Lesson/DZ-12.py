import string
text = str(input("Enter text: "))
text = text.title()
for i in string.punctuation:
    text = text.replace(i, '')
text = text.replace(" ", "")
one = str('#')
text = (one + text)
text = text[:140]
print(text)

