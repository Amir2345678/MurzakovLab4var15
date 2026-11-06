from constants import LIMITS
from logger import error_logger
def get_valid_input(prompt: str, key: str, data_type=float) -> float:
    min_val, max_val = LIMITS[key]
    while True:
        user_input = input(prompt).strip().replace(',', '.')
        try:
            value = data_type(user_input)
            if not (min_val <= value <= max_val):
                error_msg = f"Значение {key}='{value}' вне диапазона [{min_val}, {max_val}]."
                print(f"Ошибка: {error_msg}")
                error_logger.error(error_msg)
                continue
            return value
        except ValueError:
            error_msg = f"Некорректный тип данных для {key}: '{user_input}'. Ожидается число."
            print(f"Ошибка: {error_msg}")
            error_logger.error(error_msg)