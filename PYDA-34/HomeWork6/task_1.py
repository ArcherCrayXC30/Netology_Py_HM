from datetime import datetime

publishing_houses = [
    {
        'val': ('The Moscow Times', 'Wednesday, October 2, 2002'),
        'time_format': '%A, %B %d, %Y'
    },
    {
        'val': ('The Guardian', 'Friday, 11.10.13'),
        'time_format': '%A, %d.%m.%y' # дата неоднозначна так как формат не Ru_ru (издание не РФ), но выяснил по
        # календарю, что может быть пятницей
    },
    {
        'val': ('Daily News', 'Thursday, 18 August 1977'),
        'time_format': '%A, %d %B %Y'
    },
]

for item in publishing_houses:
    dt = datetime.strptime(item['val'][1], item['time_format'])
    print(f"{item['val'][0]}: {item['val'][1]} convert to datetime format --> {dt}")
