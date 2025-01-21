import os
import json
import csv
import pickle
import glob

# Задание 1: Работа с основными данными
def get_size(path):
    """Возвращает размер файла или директории."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

def traverse_directory(directory):
    """Рекурсивно обходит директорию и возвращает информацию о файлах и директориях."""
    result = []
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)
            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })
    return result

def save_to_json(data, filename):
    """Сохраняет данные в формате JSON."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    """Сохраняет данные в формате CSV."""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    """Сохраняет данные в формате Pickle."""
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

# Задание 2: Объединение данных из нескольких JSON файлов
def merge_json_files(input_files, output_file):
    """Объединяет данные из нескольких JSON файлов в один."""
    merged_data = []
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                merged_data.extend(data)
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла: {file}")
    
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)

# Задание 3: Агрегирование данных из CSV файла
def json_to_csv(json_file, csv_file):
    """Превращает данные из JSON файла в CSV файл."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    with open(csv_file, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Задание 4: Агрегирование данных из CSV файла
def calculate_total_sales(input_file, output_file):
    sales_totals = {}
    
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['название продукта']
            quantity = int(row['количество'])
            price_per_unit = float(row['цена за единицу'])
            total_sales = quantity * price_per_unit
            
            if product in sales_totals:
                sales_totals[product] += total_sales
            else:
                sales_totals[product] = total_sales
    
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for product, total_sales in sales_totals.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sales})

# Задание 5: Конвертация CSV в JSON с изменением структуры данных
def convert_csv_to_json(input_file, output_file):
    books_by_author = {}
    
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }
            if author in books_by_author:
                books_by_author[author].append(book)
            else:
                books_by_author[author] = [book]
    
    with open(output_file, 'w') as f:
        json.dump(books_by_author, f, indent=4)

# Основная функция для выполнения всех заданий
def main():
    # Задание 1: Работа с директориями
    directory_data = traverse_directory('your_directory')  # Укажите директорию
    save_to_json(directory_data, 'directory_info.json')
    save_to_csv(directory_data, 'directory_info.csv')
    save_to_pickle(directory_data, 'directory_info.pkl')
    
    # Задание 2: Объединение JSON файлов
    json_files = glob.glob('employees*.json')  # Замените шаблон на свой путь
    merge_json_files(json_files, 'all_employees.json')
    
    # Задание 3: Преобразование JSON в CSV
    json_to_csv('products.json', 'products.csv')  # Замените на ваш файл
    
    # Задание 4: Агрегирование продаж
    calculate_total_sales('sales.csv', 'total_sales.csv')  # Замените на ваш файл
    
    # Задание 5: Преобразование CSV в JSON с изменением структуры
    convert_csv_to_json('books.csv', 'books_by_author.json')  # Замените на ваш файл

if __name__ == "__main__":
    main()
