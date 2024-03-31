import string
text = (input("Enter a-z: "))
start = string.ascii_letters.find(text[0])
end = string.ascii_letters.find(text[2]) + 1
x = string.ascii_letters[start:end]
print(x)
