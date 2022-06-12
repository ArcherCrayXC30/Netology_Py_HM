my_list = ['2018-01-01', 'yandex', 'cpc', 100]

result = my_list[-1]
for val in reversed(my_list[:-1]):
    result = {val: result}

print(result)