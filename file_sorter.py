import os
import shutil

def sort_files(source_dir, destination_dir):
    """
    Функция для сортировки файлов из папок.
    """
    # Создаем папку назначения, если ее нет
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Получаем список папок в исходной директории
    subfolders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    subfolders.sort(key=lambda x: int(x))  # Сортируем папки по числовому порядку

    file_counter = 1  # Счетчик для переименования файлов

    for subfolder in subfolders:
        subfolder_path = os.path.join(source_dir, subfolder)
        files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        files.sort()  # Сортируем файлы по имени

        for file in files:
            new_file_name = f"image_{file_counter}.jpg"  # Или другое расширение
            new_file_path = os.path.join(destination_dir, new_file_name)
            shutil.move(os.path.join(subfolder_path, file), new_file_path)
            file_counter += 1

    return f"Файлы успешно отсортированы в папку: {destination_dir}"