import re

some_words_1 = 'Информационные технологии'

some_words_2 = 'Near Field Communication'


def acronim(str):
    pattern = r'\b(\w)\w+'

    return ''.join(re.findall(pattern, str)).upper()


print(acronim(some_words_1), acronim(some_words_2))
