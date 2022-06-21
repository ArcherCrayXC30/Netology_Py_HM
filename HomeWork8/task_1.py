import re

def check_car_id(car_id):
    patter = r'^([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})$'
    if re.match(patter, car_id):
        print(f"Номер: {re.match(patter, car_id).group(1)} валиден, Регион: {re.match(patter, car_id).group(2)}")
    else: print('Номер не валиден')


car_id = input("Enter Car id")

check_car_id(car_id)