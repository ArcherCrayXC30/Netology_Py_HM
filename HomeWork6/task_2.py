from datetime import datetime
import traceback
format_date = '%Y-%m-%d'

stream = ['2018-04-02', '2018-02-29', '2018-19-02']


def check_date(date_str):
    try:
        datetime.strptime(date_str, format_date)
        return True
    except ValueError:
        print(traceback.print_exc())
        return False


print(list(map(check_date, stream)))
