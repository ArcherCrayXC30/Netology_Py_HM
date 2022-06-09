print("task_4 ----->")
lenght = int(input("длина:"))
width = int(input("ширина:"))
height = int(input("высота:"))

box_1_param = 15
box_2_param = [15, 50]
skis_param = 200
6
if height > skis_param:
    print("Упаковка для лыж")

elif lenght <= box_1_param and width <= box_1_param and height <= box_1_param:
    print("Коробка №1")
elif (lenght > box_2_param[0] and lenght < box_2_param[1]) or (width > box_2_param[0] and width < box_2_param[1]) or (height > box_2_param[0] and height < box_2_param[1]):
    print("Коробка №2")
else: print("Стандартная коробка №3")