import random
import os

# Задача 1: Карма

NIRVANA_KARMA = 500

# Определение пользовательских исключений
class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")

# Функция, моделирующая один день жизни
def one_day():
    # Случайное количество кармы от 1 до 7
    day_karma = random.randint(1, 7)
    # Случайная вероятность выброса исключения
    if random.randint(1, 10) == 5:
        # Случайный выбор исключения
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma

# Основная функция симулятора
def main():
    karma = 0
    # Открываем файл для записи логов
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                karma += one_day()
            except Exception as ex:
                # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')
            if karma >= NIRVANA_KARMA:
                break
    print('Вы достигли Нирваны! ')
    print('Омм ')


# Задача 2: Чат
class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename

    def display_messages(self):
        """Отображает все сообщения из файла."""
        try:
            with open(self.filename, 'r') as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока что ничего нет\n")

    def add_message(self, name, message):
        """Добавляет новое сообщение в файл."""
        with open(self.filename, 'a') as file:
            file.write(f"{name}: {message}\n")

    def run(self):
        """Запускает основной цикл чата."""
        name = input("Как вас зовут? ")
        while True:
            print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2")
            response = input("Введите 1 или 2: ")
            if response == '1':
                self.display_messages()
            elif response == '2':
                new_message = input("Введите сообщение: ")
                self.add_message(name, new_message)
            else:
                print("Неизвестная команда\n")


# Задача 3: Счастливое число
MAGIC_NUMBER = 777

class MagicFileProcessor:
    def __init__(self, filename):
        """Инициализация с именем файла и определение пути к файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return os.path.join(os.path.abspath('.'), self.filename)

    def is_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать ошибку."""
        return random.randint(1, 13) == 7

    def pre_init(self):
        """Удаляет файл, если он существует."""
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')

    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в файл."""
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')
        except (ValueError, KeyboardInterrupt) as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.pre_init()  # Удаляет старый файл, если он существует
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


# Задача 4: Счетчик Очков в Игрe
class ScoreLimitExceededError(Exception):
    """Исключение, выбрасываемое при попытке добавить очки, превышающие лимит."""
    def __init__(self):
        super().__init__("Очки не могут быть больше 1000.")

class GameScore:
    """Класс для отслеживания очков игрока с ограничениями."""
    def __init__(self):
        """Инициализирует начальное значение очков."""
        self.score = 0

    def add_score(self, points):
        """Добавляет очки к текущему счету, проверяя лимит."""
        if self.score + points > 1000:
            raise ScoreLimitExceededError()
        self.score += points

    def subtract_score(self, points):
        """Уменьшает очки, проверяя, чтобы счет не стал отрицательным."""
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points


# Задача 5: Валидатор Пользовательских Данных
class NameError(Exception):
    def __init__(self):
        super().__init__("Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы.")

class EmailError(Exception):
    def __init__(self):
        super().__init__("Электронная почта должна содержать символ '@' и точку '.' после '@'.")

class AgeError(Exception):
    def __init__(self):
        super().__init__("Возраст должен быть целым числом от 0 до 120.")

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (len(value.split()) >= 2 and all(word[0].isupper() for word in value.split())):
            raise NameError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value.split('@')[1]:
            raise EmailError()
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and 0 <= value <= 120):
            raise AgeError()
        self._age = value

# Пример использования всех задач:

if __name__ == "__main__":
    # Задача 1
    main()

    # Задача 2
    chat = Chat()
    chat.run()

    # Задача 3
    processor = MagicFileProcessor('out_file.txt')
    processor.run()

    # Задача 4
    game_score = GameScore()
    try:
        game_score.add_score(500)
        print(f"Текущий счет: {game_score.score}")
        game_score.add_score(600)
    except ScoreLimitExceededError as e:
        print(e)
    except ValueError as e:
        print(e)

    try:
        game_score.subtract_score(600)
    except ValueError as e:
        print(e)

    # Задача 5
    try:
        user = User(name="John Doe", email="john.doe@example.com", age=25)
        print(f"User created: {user.name}, {user.email}, {user.age}")
    except (NameError, EmailError, AgeError) as e:
        print(e)
