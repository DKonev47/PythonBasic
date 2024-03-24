import string
import keyword

text = str(input("Enter Text: "))
result = True
if text[0].isdigit():                                                          # Первая цифра
    result = False
elif any(i in string.punctuation.replace('_', '') for i in text):  # Символы
    result = False
elif any(i in string.ascii_uppercase for i in text):                           # Большие буквы
    result = False
elif any(i in string.whitespace for i in text):                                # Пробелы
    result = False
elif text in keyword.kwlist:                                                   # Зарезервированные слова
    result = False
elif (text[0] == '_') and (len(text) > 1) and (text.count('_') == len(text)):
    result = False
print(text, result)
