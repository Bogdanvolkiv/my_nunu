# Задача 1: Удаление дубликатов из списка
def remove_duplicates(elements):
    duplicates = []
    for x in elements:
        if elements.count(x) > 1 and x not in duplicates:
            duplicates.append(x)
    return duplicates

# Задача 2: Поиск наибольшего числа в списке
def find_max_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Задача 3: Проверка палиндрома
def is_palindrome(string):
    string = string.lower()
    odd_chars = set()
    for char in string:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    return len(odd_chars) <= 1

# Задача 4: Генерация паролей
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Задача 5: Нахождение анаграмм
def are_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    char_count1 = {}
    char_count2 = {}
    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2

# Пример работы всех задач
if __name__ == "__main__":
    # Задача 1
    elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print("Дубликаты:", remove_duplicates(elements))

    # Задача 2
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
    print("Наибольшее число:", find_max_number(numbers))

    # Задача 3
    string = input("Введите строку для проверки палиндрома: ")
    print("Палиндром" if is_palindrome(string) else "Не палиндром")

    # Задача 4
    length = int(input("Введите длину пароля: "))
    print("Сгенерированный пароль:", generate_password(length))

    # Задача 5
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")
    print("Слова являются анаграммами" if are_anagrams(word1, word2) else "Слова не являются анаграммами")
