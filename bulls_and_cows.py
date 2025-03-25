# 1. Написать, чтобы компьютер играл с человеков в "быков и коров".
# Компьютер загадывает число из 4х РАЗНЫХ цифр (можно упростить задачу,
# не запрещая компьютеру повторять цифры)

# Человек попытка за попыткой угадывает число.
# Если цифра в попытке стоит на своем месте, она называется бык
# Если цифра есть, но стоит на другом месте, она корова
# После каждой попытки надо выдавать диагностику:
# 1 бык, 2 коровы
# Можно упростить задачу, не указывая окончания существительных
# (1 б, 3 к)

import random

# Основная функция
def Play():
    
    # Выбор длины числа для игры с защитой от выхода за пределы значений 
    while(True):
        num_choice = input('Введите длину числа (от 4 до 8): ')
        num_int = int(num_choice)
        if (4 <= num_int <= 8):
            break

    # генерируем число для игры с указанным значением 
    number = makeNumber(num_int)

    # игра
    while(True):
        answer = input('Введите число: ')

        # защита от выхода за пределы значений
        while(len(answer)!= len(number)):
            answer = input('Введите число: ')
        
        if (answer == number):
            break
        else:
            BullCow(number, answer)
    print(f'Поздравляю с победой! Загаданное число - {number}')


# Тело игры
def BullCow(number, answer):
    bull = 0
    cow = 0
    number_list = list(number)
    answer_list = list(answer)

    # цикл для подсчёта коров
    i = 0
    for _ in range(len(number_list)):
        if number_list[i] == answer_list[i]:
            bull+=1
        i+=1
    
    # двойной цикл для подсчёта быков
    i = 0
    for _ in range(len(number_list)):
        j = 0
        for _ in range(len(answer_list)):
            if number_list[i] == answer_list[j]:
                cow += 1
            j+=1
        i += 1

    print (f'Коровы - {cow} : Быки - {bull}')

# функция генерации случайного числа с неповторяющимися значениями + запись в файл
def makeNumber(num):
    numbers = '12456789'
    number_lst = []
    past_numbers = []

    while len(number_lst) < num:
        digit = random.choice(numbers)
        if digit not in number_lst:
            number_lst.append(digit)
    number = ''.join(number_lst)


    file = open('all_numbers.txt', 'r', encoding='UTF-8')
    for line in file:
        past_numbers.append(line.strip())
    file.close()

    if number in past_numbers:
        makeNumber(num)
    else:
        file = open('all_numbers.txt', 'a', encoding='UTF-8')
        file.write(f'{number}\n')
        file.close()     
        return number


Play()
