import argparse
from datetime import datetime

WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


def is_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def months(year=2000):
    return (('янв', 31), ('фев', 29 if is_leap(year) else 28), ('мар', 31),
            ('апр', 30), ('мая', 31), ('июн', 30), ('июл', 31), ('авг', 31),
            ('сен', 30), ('окт', 31), ('ноя', 30), ('дек', 31))


def parse_date(date_txt):
    try:
        week, weekday, month = date_txt.split()
    except:
        raise ValueError("Неверный формат даты")

    if not (week[0].isdigit() and 0 < int(week[0]) < 6):
        raise ValueError("Неверная неделя")

    if weekday.isdigit():
        weekday = WEEK[int(weekday) - 1]
    if weekday not in WEEK:
        raise ValueError("Неверный день недели")

    if month.isdigit():
        month = int(month)
    else:
        for i, m in enumerate(months(), 1):
            if month[:3] == m[0]:
                month = i
                break
        else:
            raise ValueError("Неверный месяц")

    return int(week[0]), weekday, month


def check_date(text_date):
    week, weekday, month = parse_date(text_date)
    year = datetime.now().year
    first_day_of_month = datetime.strptime(f'01.{month}.{year}', '%d.%m.%Y').weekday()
    current_week = WEEK[first_day_of_month:] + WEEK[:first_day_of_month]

    for i in range(months(year)[month - 1][1]):
        if weekday == current_week[i % 7]:
            week -= 1
            if not week:
                return i + 1

    raise ValueError("Невозможно определить дату")


def main():
    parser = argparse.ArgumentParser(description="Convert text date to actual date.")
    parser.add_argument("date_text", type=str, nargs='?',
                        default=f'1-й {datetime.now().strftime("%A")} {datetime.now().strftime("%B")}',
                        help="Text date to convert")

    args = parser.parse_args()
    try:
        day = check_date(args.date_text)
        current_year = datetime.now().year
        result_date = datetime(current_year, parse_date(args.date_text)[2], day)
        print(result_date.strftime('%Y-%m-%d'))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
