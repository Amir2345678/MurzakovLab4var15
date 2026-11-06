from menu import run_calculation
from logger import error_logger
if __name__ == "__main__":
    try:
        run_calculation()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        error_logger.error(f"Критическая ошибка: {str(e)}", exc_info=True)
        print(f"\nПроизошла непредвиденная ошибка. Подробности в файле input_errors.log")


