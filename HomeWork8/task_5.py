import re

some_text = 'Эталонной реализацией Python является интерпретатор CPython,' \
            ' поддерживающий большинство активно используемых платформ.' \
            ' Он распространяется под свободной лицензией Python Software Foundation License,' \
            ' позволяющей использовать его без ограничений в любых приложениях, включая проприетарные.'


def count_letter(text):
    lower_text = text.lower()
    vowels = r'\b([aeiouаеёиоуыэюя])\w+'
    consonants = r'\b([бвгдзклмнпрстфхbcdfghjklmnpqrstvwxyz])\w+'
    return f"Слов на гласные: {len(re.findall(vowels, lower_text))}, Слов на согласные: {len(re.findall(consonants, lower_text))} "

print(count_letter(some_text))
