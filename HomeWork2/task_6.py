input_str = input("Введите числа через пробел:")

split_str = input_str.split(' ')
result_array = []

for i in range(len(split_str)):
    if i != split_str.index(split_str[i]):
        result_array.append(int(split_str[i]))

print(sorted(set(result_array)))