# word_count.py
def count_word_occurrences(words):
    """
    Подсчитывает количество повторений каждого слова в списке.
    Аргументы:
    words -- список слов
    Возвращает:
    Словарь с количеством повторений каждого слова
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


# remove_duplicates.py
def remove_consecutive_duplicates(s):
    """
    Удаляет дублирующиеся подряд символы в строке.
    Аргументы:
    s -- строка
    Возвращает:
    Строку без дублирующихся подряд символов
    """
    if not s:
        return s
    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)


# unique_to_both_lists.py
def unique_to_both_lists(list1, list2):
    """
    Нахождение уникальных элементов для обоих списков.
    Аргументы:
    list1 -- первый список
    list2 -- второй список
    Возвращает:
    Список уникальных элементов, которые присутствуют только в одном из двух списков
    """
    set1, set2 = set(list1), set(list2)
    unique_elements = (set1 - set2) | (set2 - set1)
    return list(unique_elements)


# date_validator.py
from datetime import datetime

def _is_leap_year(year):
    """
    Возвращает True, если год високосный, иначе False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(date_str):
    """
    Проверяет, является ли дата в формате DD.MM.YYYY валидной.
    """
    if len(date_str) != 10:
        return False
    parts = date_str.split('.')
    if len(parts) != 3:
        return False
    try:
        day, month, year = map(int, parts)
    except ValueError:
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if _is_leap_year(year) and day > 29:
            return False
        elif not _is_leap_year(year) and day > 28:
            return False
    return True


# chess.py
def are_queens_safe(positions):
    """
    Проверяет, не бьют ли друг друга ферзи на доске 8x8.
    Аргументы:
    positions -- список кортежей, где каждый кортеж содержит координаты ферзя (строка, столбец)
    Возвращает:
    True, если ферзи не бьют друг друга; False в противном случае
    """
    def is_under_attack(row, col):
        """
        Проверяет, атакуется ли позиция (row, col) другими ферзями.
        """
        for i in range(8):
            if i != row:
                if (positions[i][1] == col or
                    abs(positions[i][0] - row) == abs(positions[i][1] - col)):
                    return True
        return False

    for i in range(8):
        if is_under_attack(positions[i][0], positions[i][1]):
            return False
    return True


# Пример использования всех модулей:

# 1. Пример для подсчета слов
words = ['apple', 'banana', 'apple', 'orange']
print(count_word_occurrences(words))  # Output: {'apple': 2, 'banana': 1, 'orange': 1}

# 2. Пример для удаления дублирующихся символов
s = 'aaabbcaaa'
print(remove_consecutive_duplicates(s))  # Output: 'abca'

# 3. Пример для нахождения уникальных элементов
list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(unique_to_both_lists(list1, list2))  # Output: [1, 2, 4, 5]

# 4. Пример для проверки даты
date = "29.02.2024"
print(is_valid_date(date))  # Output: True

# 5. Пример для проверки ферзей
positions = [(1, 1), (2, 5), (3, 8), (4, 3), (5, 7), (6, 2), (7, 4), (8, 6)]
print(are_queens_safe(positions))  # Output: True
