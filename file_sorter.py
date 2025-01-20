import re
import os
from collections import defaultdict
from datetime import datetime

# Функция для обработки лога и подсчета количества ошибок 404 для каждой минуты
def parse_nginx_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.readlines()
