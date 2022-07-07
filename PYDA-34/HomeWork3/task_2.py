queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

queries_dict = {}
all_queries_leng = len(queries)

for val in queries:
    word_arr = val.split(" ")
    if len(word_arr) in queries_dict:
        queries_dict[len(word_arr)] += 1
    else:
        queries_dict[len(word_arr)] = 1

for key, val in queries_dict.items():
    print(f'Поисковых запросов, содержащих {key} слов(а): {val/all_queries_leng:2.2%}')
