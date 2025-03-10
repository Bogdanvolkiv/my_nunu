# Пользователь вводит размеры рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

# Внешний цикл — строки рамки
for row in range(height):
    # Внутренний цикл — символы в строке
    for col in range(width):
        # Если это первый или последний столбец
        if col == 0 or col == width - 1:
            print('|', end='')  # Вертикальная граница
        # Если это первая или последняя строка
        elif row == 0 or row == height - 1:
            print('-', end='')  # Горизонтальная граница
        else:
            print(' ', end='')  # Внутреннее пространство рамки
    print()  # Переход на новую строку
