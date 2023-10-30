from datetime import datetime
from currency_data import get_currency_rate

# Введите дату
input_date = '2023/09/01'

# Преобразуйте строку с датой в объект datetime
date_to_find = datetime.strptime(input_date, '%Y/%m/%d')

# Имя файла с данными о курсе валюты
file_name = 'dataset.csv'  # Замените на имя вашего файла

# Получите курс валюты на указанную дату
rate = get_currency_rate(date_to_find, file_name)

if rate is not None:
    print(f"Курс валюты USD на {input_date}: {rate}")
else:
    print(f"Данные о курсе валюты USD на {input_date} отсутствуют.")
