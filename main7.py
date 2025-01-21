import os
import zipfile
import time

# Задача 1. Функция группового переименования файлов
def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
    """
    Переименовывает файлы в указанном каталоге.
    :param directory: Путь к каталогу с файлами.
    :param final_name: Конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param old_extension: Расширение исходного файла.
    :param new_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени (начало, конец).
    """
    # Проверяем существование каталога
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")
    
    # Получаем список файлов с указанным расширением
    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
    if not files:
        print("Файлы с указанным расширением не найдены.")
        return

    # Определяем формат номера с ведущими нулями
    format_string = f"{{:0{num_digits}d}}"

    # Перебираем файлы и переименовываем их
    for index, file_name in enumerate(files, start=1):
        # Извлекаем базовое имя файла без расширения
        base_name = os.path.splitext(file_name)[0]
        
        # Извлекаем часть имени файла по заданному диапазону
        if name_range:
            start, end = name_range
            extracted_name = base_name[start-1:end]  # Индексы диапазона начинаются с 0
        else:
            extracted_name = base_name
        
        # Формируем новое имя файла
        new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
        
        # Полные пути для старого и нового файла
        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)
        
        # Переименование файла
        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{file_name}' в '{new_file_name}'")

# Задача 2. Создание архива каталога
def zip_directory(source_dir, output_zip):
    """
    Создает архив .zip из указанного каталога.
    :param source_dir: Путь к исходному каталогу для архивирования.
    :param output_zip: Путь к целевому архиву .zip.
    """
    # Создаем объект ZipFile для записи архива
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Проходим по всем файлам и папкам в исходном каталоге
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Полный путь к текущему файлу
                file_path = os.path.join(root, file)
                # Добавляем файл в архив с путем относительно исходного каталога
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

# Задача 3. Удаление старых файлов
def delete_old_files(directory, days_old):
    """
    Удаляет файлы в указанном каталоге, которые не изменялись более заданного количества дней.
    :param directory: Путь к каталогу, в котором нужно удалить старые файлы.
    :param days_old: Количество дней, после которых файлы считаются старыми.
    """
    now = time.time()  # Текущее время в секундах с начала эпохи
    cutoff = now - (days_old * 86400)  # Преобразуем количество дней в секунды (86400 секунд в дне)
    
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  # Полный путь к файлу
            file_mod_time = os.path.getmtime(file_path)  # Время последнего изменения файла
            # Если время последнего изменения меньше порогового значения, удаляем файл
            if file_mod_time < cutoff:
                os.remove(file_path)  # Удаляем файл
                print(f"Удален файл: {file_path}")

# Задача 4. Поиск файлов по расширению
def find_files_by_extension(directory, extension):
    """
    Находит и перечисляет все файлы с заданным расширением в указанном каталоге и всех его подкаталогах.
    :param directory: Путь к каталогу, в котором нужно искать файлы.
    :param extension: Расширение файлов для поиска (например, '.txt').
    """
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, заканчивается ли имя файла на заданное расширение
            if file.endswith(extension):
                # Формируем полный путь к файлу и выводим его
                print(os.path.join(root, file))

# Пример использования функций:
if __name__ == "__main__":
    # Пример использования функции для переименования файлов
    batch_rename_files('path_to_directory', 'final_name', 3, '.txt', '.md', [3, 6])

    # Пример использования функции для создания архива каталога
    zip_directory('path_to_directory', 'output.zip')

    # Пример использования функции для удаления старых файлов
    delete_old_files('path_to_directory', 30)

    # Пример использования функции для поиска файлов по расширению
    find_files_by_extension('path_to_directory', '.txt')
