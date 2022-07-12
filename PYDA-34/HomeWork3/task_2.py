import time

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
start1 = time.time()
for val in queries:
    word_arr = val.split(" ")
    if len(word_arr) in queries_dict:
        queries_dict[len(word_arr)] += 1
    else:
        queries_dict[len(word_arr)] = 1

for key, val in queries_dict.items():
    print(f'Поисковых запросов, содержащих {key} слов(а): {val/all_queries_leng:2.2%}')
end1 = time.time()

start2 = time.time()
len_q = [len(query.split()) for query in queries]
for i in sorted(set(len_q)):
    print(f"Поисковых запросов, содержащих {i} слов(а): {len_q.count(i)/all_queries_leng:.2%}")
end2 = time.time()

print(start1, end1, '---', end1 - start1)
print(start2, end2, '---', end2 - start2)