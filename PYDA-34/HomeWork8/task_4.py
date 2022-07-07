import re

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']


def cut_domain(email):
    pattern = r'\@(.*)'
    return re.findall(pattern, email)[0]

domains = {}

for email in emails:
    res = cut_domain(email)
    if res in domains.keys():
        domains[res] += 1
    else:
        domains[res] = 1

list = ", ".join([f"{domain[0]}: {domain[1]}" for domain in domains.items()])

print(list)
