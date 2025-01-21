import random


# Задача 1. Апгрейд калькулятора
def digits_summ(num):
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10
    print('Сумма цифр:', summ)

def max_digit(num):
    maximum = 0
    while num > 0:
        digit = num % 10
        if digit > maximum:
            maximum = digit
        num //= 10
    print('Максимальная цифра:', maximum)

def min_digit(num):
    minimum = num % 10
    while num > 0:
        digit = num % 10
        if digit < minimum:
            minimum = digit
        num //= 10
    print('Минимальная цифра:', minimum)


# Задача 2. Игры
def rock_paper_scissors():
    player = input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: ")
    computer = random.choice([1, 2, 3])
    
    if player == "1":
        player_choice = "Камень"
    elif player == "2":
        player_choice = "Ножницы"
    elif player == "3":
        player_choice = "Бумага"
    else:
        print("Неверный выбор!")
        return

    if computer == 1:
        computer_choice = "Камень"
    elif computer == 2:
        computer_choice = "Ножницы"
    elif computer == 3:
        computer_choice = "Бумага"

    print(f"Компьютер выбрал: {computer_choice}")

    if player == str(computer):
        print("Ничья!")
    elif (player == "1" and computer == 2) or (player == "2" and computer == 3) or (player == "3" and computer == 1):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

def guess_the_number():
    number = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    
    while True:
        guess_num = int(input('Введите число: '))
        if guess_num > number:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        elif guess_num < number:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        else:
            print('Поздравляю, вы угадали!')
            break


# Задача 3. Число наоборот
def reversal(x):
    revers_x = 0
    while x > 0:
        revers_x = revers_x * 10 + x % 10
        x = x // 10
    return revers_x

# Задача 4. Функция максимума
def max_of_2(number_1, number_2):
    if number_1 > number_2:
        return number_1
    return number_2

def max_of_3(number_1, number_2, number_3):
    return max_of_2(max_of_2(number_1, number_2), number_3)


# Задача 5. Яйца
def calculate_danger(x):
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(max_danger):
    d_min = 0
    d_max = 4
    while (d_max - d_min) > 1e-9:
        d_middle = (d_min + d_max) / 2
        middle_danger = calculate_danger(d_middle)
        
        if abs(middle_danger) <= max_danger:
            return d_middle
        
        if middle_danger > 0:
            d_min = d_middle
        else:
            d_max = d_middle


# Основное меню
def main_menu():
    while True:
        print("\nЧто хотите сделать?")
        print("1 - Апгрейд калькулятора")
        print("2 - Игры")
        print("3 - Число наоборот")
        print("4 - Максимальное число")
        print("5 - Яйца")
        print("6 - Выход")
        
        choice = int(input("Выберите действие: "))
        
        if choice == 1:
            num = int(input('Введите число: '))
            action = int(input('Введите номер действия: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: '))
            if action == 1:
                digits_summ(num)
            elif action == 2:
                max_digit(num)
            elif action == 3:
                min_digit(num)
            else:
                print('Ошибка: неверная команда.')
                
        elif choice == 2:
            game_choice = int(input("\nВо что хотите поиграть?\n1 - Камень, ножницы, бумага\n2 - Угадай число\n3 - Назад\n"))
            if game_choice == 1:
                rock_paper_scissors()
            elif game_choice == 2:
                guess_the_number()
            elif game_choice == 3:
                continue
            else:
                print("Неверный выбор!")

        elif choice == 3:
            num_1 = int(input('Введите первое число: '))
            num_2 = int(input('Введите второе число: '))
            revers_num1 = reversal(num_1)
            revers_num2 = reversal(num_2)

            print('\nПервое число наоборот:', revers_num1)
            print('Второе число наоборот:', revers_num2)

            amount = revers_num1 + revers_num2
            revers_summ = reversal(amount)

            print('\nСумма:', amount)
            print('Сумма наоборот:', revers_summ)

        elif choice == 4:
            digit_1 = int(input('Введите первое число: '))
            digit_2 = int(input('Введите второе число: '))
            digit_3 = int(input('Введите третье число: '))
            print('Самое большое число:', max_of_3(digit_1, digit_2, digit_3))

        elif choice == 5:
            try:
                max_danger = float(input('Введите максимально допустимый уровень опасности: '))
                if max_danger <= 0:
                    print('Вы ввели недопустимое значение! Попробуйте еще раз.')
                else:
                    safe_depth = find_safe_depth(max_danger)
                    print(f'Приблизительная глубина безопасной кладки: {safe_depth:.9f} м')
            except ValueError:
                print('Ошибка: введено не число!')

        elif choice == 6:
            print("Выход из программы.")
            break
        else:
            print("Неверная команда! Попробуйте снова.")


main_menu()
