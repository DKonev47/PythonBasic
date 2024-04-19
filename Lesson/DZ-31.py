import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    while html.count('>') > 0:
        start = html[html.find('>') + 1:]
        end = html[:html.find('<')]
        html = (end + start)

    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(html)


html_text = 'C:\\Users\\DKone\\PycharmProjects\\pythonProjectJunkerPython\\draft.html'
delete_html_tags(html_text)
