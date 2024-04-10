def first_word(text):
    """ Пошук першого слова """
    import string
    sim_del = string.punctuation.replace('\'', '')
    for i in sim_del:
        text = text.replace(i, " ")
    text = text.split()
    res = text[0]
    return res


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
