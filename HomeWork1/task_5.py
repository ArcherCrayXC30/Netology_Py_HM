print("task_5 ----->")
ticket_number = int(input("Enter 6-digit number: "))
part_1 = ticket_number // 1000
part_2 = ticket_number % 1000
sum_1 = 0
sum_2 = 0
for i in str(part_1):
    sum_1 += int(i)
for i in str(part_2):
    sum_2 += int(i)

if sum_1 == sum_2:
    print("Счастливый билет")

else: print("Несчастливый билет")