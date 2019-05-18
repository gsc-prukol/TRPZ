# Напишіть гру Вгадайку. Програма за допомогою рандомізатора 
# загадує ціле число від 0 до 100. Користувач з консолі вводить 
# передбачуване загадане число, програма повідомляє більше, 
# менше або вгадав. Якщо користувач не вгадав, то програма 
# пропонує спробувати вгадати знову в уточненому діапазоні 
# (з урахуванням попередніх відповідей користувача (наприклад, 
# "Менше, спробуйте в діапазоні [33, 88]")). 
# Не забувайте продумати захист від дурня.

import random
minRange, maxRange = 0, 100 
secret = random.randint(minRange, maxRange)
attemptStr = input( f'Введіть ціле число в діапазоні [{minRange}, {maxRange}].\n')
attempt = maxRange + 10

while attempt != secret:
    if len(attemptStr) < 20 and attemptStr.isdigit():
        attempt = int(attemptStr)
        if attempt >= minRange and attempt <= maxRange:
            if attempt < secret:
                print('Більше.', end = '')
                minRange = attempt + 1
            elif attempt > secret:
                print('Менше.', end ='')
                maxRange = attempt - 1
            else:
                continue
        else:
            print('Ви ввели число, що знаходиться за межами діапазону.', end = '')
    else:
        print('Ввід некоректний.', end = '')
    print(' Будь ласка, спробуйте знову.', end = '')
    attemptStr = input( f' Введіть ціле число в діапазоні [{minRange}, {maxRange}].\n')
else:
    print('Вітаю, Ви виграли.')