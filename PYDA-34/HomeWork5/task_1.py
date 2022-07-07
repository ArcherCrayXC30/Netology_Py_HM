import json


def prepare_line(line_in_file):
    return line_in_file.strip()


purchases = {}
with open('data/purchase_log.txt', 'r') as file:
    next(file)
    for line in file:
        data_ = json.loads(line)
        purchases[data_['user_id']] = data_['category']

with open('data/visit_log.csv') as log_file:
    with open('data/funnel.csv', 'w') as result_file:
        first = prepare_line(next(log_file))
        result_file.write(first + ',category\n')
        for log_line in log_file:
            prep_line = prepare_line(log_line)
            user_id = prep_line.split(',')[0]
            if user_id in purchases.keys():
                line_to_write = f"{prep_line},{purchases[user_id]}\n"
                result_file.write(line_to_write)
            else:
                result_file.write(log_line)