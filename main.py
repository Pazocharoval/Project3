from file_sorter import sort_files
import config

def main():
    """
    Главная функция запуска проекта.
    """
    source = config.SOURCE_DIR
    destination = config.DESTINATION_DIR

    try:
        result = sort_files(source, destination)
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()