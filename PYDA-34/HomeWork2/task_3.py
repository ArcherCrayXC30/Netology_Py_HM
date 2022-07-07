boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")

else:
    sort_boys = sorted(boys)
    sort_girls = sorted(girls)

    for i in range(len(boys)):
        print(f'{sort_boys[i]} и {sort_girls[i]}')