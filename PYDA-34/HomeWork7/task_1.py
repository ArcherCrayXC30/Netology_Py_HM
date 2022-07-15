from libs.exchange import Rate


class ExtendRate(Rate):
    def max_rate_name(self):
        currency_dict = list(self.exchange_rates().values())
        print(currency_dict)
        max_val = max(currency_dict, key=lambda key: key['Value'])

        return max_val['Name']



rate = ExtendRate()
name_max_currency = rate.max_rate_name()

print(name_max_currency)
