import os

def count_lines_in_py_files(directory):
    total_lines = 0
    # Проходим по всем файлам и папкам в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Проверяем, что файл имеет расширение .py
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        total_lines += len(lines)  # Считаем количество строк
                except Exception as e:
                    print(f"Не удалось прочитать файл {file_path}: {e}")
    
    return total_lines

if __name__ == '__main__':
    directory = input("Введите путь к папке: ")
    total_lines = count_lines_in_py_files(directory)
    print(f"Общее количество строк во всех .py файлах: {total_lines}")