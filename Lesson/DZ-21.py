def is_palindrome(text):
    import string
    text = text.lower()
    symbols_to_remove = string.punctuation
    for i in symbols_to_remove:
        text = text.replace(i, "")
        symbols_to_remove = string.whitespace
    for i in symbols_to_remove:
        text = text.replace(i, "")
    text = list(text)
    end = list(reversed(text))
    return text == end


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
