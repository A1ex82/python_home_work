import re
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.ERROR, filename='date_errors.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

months = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5,
    'июня': 6, 'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
}

weekdays = {
    'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6
}


def parse_date(text):
    try:

        match = re.match(r"(\d+)-[йя] (\w+) (\w+)", text)
        if not match:
            raise ValueError(f"Неверный формат текста: {text}")

        week_number = int(match.group(1))
        weekday = match.group(2)
        month = match.group(3)

        if weekday not in weekdays or month not in months:
            raise ValueError(f"Неверный день недели или месяц: {text}")

        current_year = datetime.now().year

        first_date_of_month = datetime(current_year, months[month], 1)
        first_weekday_of_month = first_date_of_month.weekday()

        if weekdays[weekday] >= first_weekday_of_month:
            day = (weekdays[weekday] - first_weekday_of_month) + 1 + (week_number - 1) * 7
        else:
            day = (7 - first_weekday_of_month + weekdays[weekday]) + 1 + (week_number - 1) * 7

        # Проверка корректности полученной даты
        final_date = datetime(current_year, months[month], day)
        if final_date.month != months[month]:
            raise ValueError(f"Дата выходит за пределы месяца: {text}")

        return final_date

    except Exception as e:
        logging.error(e)
        return None


texts = ["1-й четверг ноября", "3-я среда мая", "5-й вторник января"]

for text in texts:
    result = parse_date(text)
    if result:
        print(f"Текст: {text} -> Дата: {result.strftime('%Y-%m-%d')}")
    else:
        print(f"Ошибка при обработке текста: {text}")
