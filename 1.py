#1 задание
'''print('Если хотите остановиться напишите 0')
while True:
    year = int(input('Введите год:'))

    if year == 0:
        break
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")'''

#2 задание
'''number = input()

if len(number) != 6:
    print("Ошибка! Номер должен быть шестизначным")
else:
    sum1 = int(number[0]) + int(number[1]) + int(number[2])
    sum2 = int(number[3]) + int(number[4]) + int(number[5])
    
    if sum1 == sum2:
        print("счастливый")
    else:
        print("несчастливый")'''