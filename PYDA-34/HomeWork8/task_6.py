import re



def check_phone(phone):
    pattern_phone = r'^(\+7|7|8)?[\s\-]?\(?([489][0-9]{2})\)?[\s\-]?([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})$'
    res = re.findall(pattern_phone, phone)[0]
    if res:
        return f"+7-{res[1]}-{res[2]}-{res[3]}-{res[4]}"
    else:
        return "Номер не валиден"

phone_input = input("Phone number")

res = check_phone(phone_input)

print(res)