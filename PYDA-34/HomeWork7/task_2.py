from libs.exchange import Rate


class RateWithDiff(Rate):
    """
    Потомок класса Rate с переопределением метода make_format
    Добавлен атрибут diff - выбор формата вывода - True - разница в курсе, False - текущий курс
    """
    def __init__(self, diff=False, format='value'):
        self.diff = diff
        self.format = format

    # переопределения родительского метода
    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                if self.diff:
                    return round(response[currency]['Value'] - response[currency]['Previous'], 3)
                else:
                    return response[currency]['Value']

        return 'Error'


check_1 = RateWithDiff(diff=True, format='full')
check_2 = RateWithDiff(format='full')
check_3 = RateWithDiff(diff=True)
check_4 = RateWithDiff(diff=False)
res_1 = check_1.eur()
res_2 = check_2.eur()
res_3 = check_3.eur()
res_4 = check_4.eur()

print(f"{res_1} \n{res_2} \n{res_3} \n{res_4}")