print("task_3 ----->")
day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения: ")
zodiac = [
    {
        "name": "Овен",
        "start": {"day": 21, "month": "март"},
        "end": {"day": 20, "month": "апрель"}
    },
    {
        "name": "Телец",
        "start": {"day": 21, "month": "апрель"},
        "end": {"day": 21, "month": "май"}
    },
    {
        "name": "Близнецы",
        "start": {"day": 22, "month": "май"},
        "end": {"day": 21, "month": "июнь"}
    },
    {
        "name": "Рак",
        "start": {"day": 22, "month": "июнь"},
        "end": {"day": 22, "month": "июль"}
    },
    {
        "name": "Лев",
        "start": {"day": 23, "month": "июль"},
        "end": {"day": 23, "month": "август"}
    },
    {
        "name": "Дева",
        "start": {"day": 24, "month": "август"},
        "end": {"day": 22, "month": "сентябрь"}
    },
    {
        "name": "Весы",
        "start": {"day": 23, "month": "сентябрь"},
        "end": {"day": 23, "month": "октябрь"}
    },
    {
        "name": "Скорпион",
        "start": {"day": 24, "month": "октябрь"},
        "end": {"day": 22, "month": "ноябрь"}
    },
    {
        "name": "Стрелец",
        "start": {"day": 23, "month": "ноябрь"},
        "end": {"day": 21, "month": "декабрь"}
    },
    {
        "name": "Козерог",
        "start": {"day": 22, "month": "декабрь"},
        "end": {"day": 20, "month": "январь"}
    },
    {
        "name": "Водолей",
        "start": {"day": 21, "month": "январь"},
        "end": {"day": 18, "month": "февраль"}
    },
    {
        "name": "Рыбы",
        "start": {"day": 19, "month": "февраль"},
        "end": {"day": 20, "month": "март"}
    }
]
for item in zodiac:
    if (month == item["start"]["month"] and day > item["start"]["day"]) or (month == item["end"]["month"] and day < item["end"]["day"]):
        print("Ваш знак зодиака:", item["name"])