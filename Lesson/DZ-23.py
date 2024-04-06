def popular_words(text, words):
    text = text.lower()
    text = text.split(' ')
    dict1 = {}
    for i in words:
        dict1[i] = text.count(i)
    return dict1


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
