def correct_sentence(text):
    text_start = text[:1]
    text_end = text[1:]
    text1 = text_start.title()
    text2 = (text1 + text_end)
    if not (text2.endswith('.')):
        text2 += '.'
        return text2
    return text2


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
