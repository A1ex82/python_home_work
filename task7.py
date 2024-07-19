import logging
import argparse

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def get_numeric_input():
    while True:
        user_input = input("Введите число (целое или вещественное): ")
        try:
            value = int(user_input)
            logging.info(f"Вы ввели целое число: {value}")
            return value
        except ValueError:
            try:
                value = float(user_input)
                logging.info(f"Вы ввели вещественное число: {value}")
                return value
            except ValueError:
                logging.error(f"Ошибка: введенное значение '{user_input}' не является числом.")
                print("Ошибка: введенное значение не является числом. Попробуйте еще раз.")

def main():
    parser = argparse.ArgumentParser(description='Запрашивает числовые данные от пользователя.')
    args = parser.parse_args()

    numeric_value = get_numeric_input()
    print(f"Вы ввели корректное число: {numeric_value}")

if __name__ == "__main__":
    main()
