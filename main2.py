from fractions import Fraction

def find_gcd():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    while b != 0:
        a, b = b, a % b
    print("НОД:", a)

def decimal_to_hex():
    hex_digits = '0123456789ABCDEF'
    number = int(input("Введите число: "))
    if number == 0:
        print("Шестнадцатеричное представление: 0")
    else:
        is_negative = number < 0
        if is_negative:
            number = -number
        hex_string = ''
        while number > 0:
            remainder = number % 16
            hex_string = hex_digits[remainder] + hex_string
            number //= 16
        if is_negative:
            hex_string = '-' + hex_string
        print("Шестнадцатеричное представление:", hex_string)

def integer_to_roman():
    num = int(input("Введите целое число: "))
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    print("Римское представление:", roman_num)

def fraction_operations():
    frac1 = input("Введите первую дробь (a/b): ")
    frac2 = input("Введите вторую дробь (a/b): ")
    numerator1, denominator1 = map(int, frac1.split('/'))
    numerator2, denominator2 = map(int, frac2.split('/'))
    f1 = Fraction(numerator1, denominator1)
    f2 = Fraction(numerator2, denominator2)
    sum_frac = f1 + f2
    product_frac = f1 * f2
    print("Сумма:", sum_frac)
    print("Произведение:", product_frac)

def main():
    while True:
        print("\nВыберите задачу:")
        print("1. Нахождение НОД двух чисел")
        print("2. Преобразование числа в шестнадцатеричное представление")
        print("3. Перевод числа в римское представление")
        print("4. Сумма и произведение дробей")
        print("5. Выход")
        choice = input("Введите номер задачи: ")
        
        if choice == '1':
            find_gcd()
        elif choice == '2':
            decimal_to_hex()
        elif choice == '3':
            integer_to_roman()
        elif choice == '4':
            fraction_operations()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск программы
main()
