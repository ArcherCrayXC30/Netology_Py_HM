countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

for county in countries_temperature:
    mean_val_far = sum(county[1])/len(county[1])
    mean_cels = round((mean_val_far - 32) / 1.8, 2)
    print(f'{county[0]} - {mean_cels} C')