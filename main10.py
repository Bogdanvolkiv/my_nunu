import random

# Задача 1: Отцы, матери и дети

class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        """Сообщает информацию о родителе"""
        print(f"Меня зовут {self.name}, мне {self.age} лет")

    def add_child(self, child):
        """Добавляет ребёнка в список детей, если разница в возрасте больше 16 лет"""
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name}, так как разница в возрасте слишком мала.")

    def feed(self, child):
        """Кормит ребёнка, изменяя его состояние голода"""
        if child in self.children:
            child.hungry = False
            print(f"{self.name} покормил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def calm(self, child):
        """Успокаивает ребёнка, изменяя его состояние спокойствия"""
        if child in self.children:
            child.calm = True
            print(f"{self.name} успокоил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def list_children(self):
        """Выводит информацию обо всех детях родителя"""
        if self.children:
            print(f"У {self.name} есть следующие дети:")
            for child in self.children:
                print(f" - {child}")
        else:
            print(f"У {self.name} нет детей.")


class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.calm = False  # Ребёнок по умолчанию не спокоен
        self.hungry = True  # Ребёнок по умолчанию голоден

    def get_status(self):
        """Сообщает текущее состояние ребёнка"""
        calm_status = "спокоен" if self.calm else "не спокоен"
        hungry_status = "сыт" if not self.hungry else "голоден"
        print(f"Ребёнок {self.name} {calm_status} и {hungry_status}.")

    def __str__(self):
        """Представление объекта ребёнка в виде строки"""
        return f"Ребёнок {self.name}, {self.age} лет"


# Пример использования задачи 1
parent = Parent("Иван", 40)
child1 = Child("Анна", 20)
child2 = Child("Петя", 10)
child3 = Child("Маша", 3)

for child in [child1, child2, child3]:
    parent.add_child(child)

parent.info()
parent.list_children()

for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()


# Задача 2: Совместное проживание

class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):
        """Покупка еды: увеличивает количество еды и уменьшает количество денег."""
        if self.money >= price:
            self.food += quantity
            self.money -= price
            print(f"Купили {quantity} единиц еды за {price} денег.")
        else:
            print("Недостаточно денег для покупки еды!")

    def earn_money(self, salary):
        """Заработок денег: увеличивает количество денег в доме."""
        self.money += salary
        print(f"Заработали {salary} денег.")


class Human:
    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.house = house

    def eat(self):
        """Метод, который увеличивает сытость человека и уменьшает количество еды в доме."""
        if self.house.food >= 10:
            self.hunger += 10
            self.house.food -= 10
            print(f"{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.")
        else:
            print(f"{self.name} хотел поесть, но в доме недостаточно еды!")

    def work(self):
        """Метод, который уменьшает сытость человека и увеличивает количество денег в доме."""
        self.hunger -= 10
        self.house.earn_money(50)
        print(f"{self.name} поработал. Сытость уменьшилась до {self.hunger}.")

    def play(self):
        """Метод, который уменьшает сытость человека."""
        self.hunger -= 5
        print(f"{self.name} поиграл. Сытость уменьшилась до {self.hunger}.")

    def shop_for_food(self):
        """Метод, который покупает еду за деньги."""
        self.house.buy_food(15, 50)

    def live_day(self):
        """Метод, который моделирует один день жизни человека."""
        cube = random.randint(1, 6)
        print(f"\nСегодняшний кубик: {cube}")
        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

        if self.hunger <= 0:
            print(f"{self.name} умер от голода.")
            return False
        return True


# Пример использования задачи 2
house1 = House()
human1 = Human("Артем", house1)
human2 = Human("Даша", house1)

for day in range(1, 366):  # Моделируем 365 дней
    print(f"\nДень {day}")
    if not human1.live_day() or not human2.live_day():
        print(f"Человек умер на {day} день.")
        break
else:
    print("Оба человека выжили и прожили 365 дней.")


# Задача 3: Крестики-нолики

class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = " "  # Символ клетки ('X', 'O' или пробел)
        self.occupied = False  # Статус занятости клетки


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display_board(self):
        """Отображает игровую доску."""
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |")
        print("-------------")

    def change_cell(self, cell_number, symbol):
        """Изменяет символ клетки, если она не занята."""
        cell = self.cells[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True

    def check_game_over(self):
        """Проверяет, завершена ли игра (выигрыш или ничья)."""
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in win_positions:
            if self.cells[pos[0]].symbol != " " and self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == self.cells[pos[2]].symbol:
                return True
        return False

    def reset_board(self):
        """Сбрасывает игровую доску для новой игры."""
        for cell in self.cells:
            cell.symbol = " "
            cell.occupied = False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        """Запрашивает ход игрока и проверяет корректность ввода."""
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки для вашего хода (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError
                return move
            except ValueError:
                print("Неправильный ввод. Пожалуйста, введите число от 1 до 9.")


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()

    def launch_move(self, player):
        """Выполняет ход текущего игрока."""
        while True:
            self.board.display_board()
           
