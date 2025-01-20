# Функция для сохранения результатов в файл
def save_error_counts_to_file(error_counts, output_file):
    with open(output_file, 'w') as file:
        for timestamp, count in sorted(error_counts.items()):
            file.write(f"{timestamp} - Ошибки 404: {count}\n")

# Главная функция для обработки лога и сохранения результатов
def main():
    log_file = f'{os.getcwd()}/logs/nginx_log'  # Замените путь на путь вашего файла
    output_file = f'{os.getcwd()}/404_errors_per_minute.txt'

    error_counts = parse_nginx_log(log_file)
    save_error_counts_to_file(error_counts, output_file)
    print(f"Результаты сохранены в {output_file}")

# Выполнение скрипта
if __name__ == "__main__":
    main()
