import re

some_string = 'Напишите функцию функцию, которая будет будет будет будет ' \
              'удалять все все все все последовательные повторы слов из из из из' \
              ' заданной строки строки при помощи регулярных выражений.'


def remove_repeats(str):
    return re.sub(r'\b([^\W\d_]+)(\s+\1)+\b', r'\1', re.sub(r'\W+', ' ', str).strip(), flags=re.I)


print(remove_repeats(some_string))
