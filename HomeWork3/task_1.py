ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

all_values = []

for val in ids.values():
    all_values += val

uniq_val = set(all_values)

print(uniq_val)