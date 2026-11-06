from constants import MATERIALS
from validation import get_valid_input
from operation import calculate_torsion
from logger import error_logger
def print_main_menu():
    print("\n" + "="*40)
    print("РАСЧЁТ ВАЛА НА КРУЧЕНИЕ")
    print("="*40)
    print("Выберите материал:")
    for key, (name, tau) in MATERIALS.items():
        print(f"  {key} — {name} ([τ] = {tau} МПа)")
def run_calculation():
    print_main_menu()
    while True:
        choice = input("\nВведите номер материала (1-3): ").strip()
        if choice in MATERIALS:
            material_name, tau_allow = MATERIALS[choice]
            break
        else:
            error_msg = f"Неверный выбор материала: '{choice}'"
            print("Ошибка: Выберите 1, 2 или 3.")
            error_logger.error(error_msg)
    print(f"\nВыбран материал: {material_name} (Допустимое напряжение [τ] = {tau_allow} МПа)")
    print("Введите параметры вала (диапазоны указаны в скобках):")
    T = get_valid_input("Крутящий момент T, Н-м [0.1..10000]: ", "T")
    d = get_valid_input("Диаметр вала d, мм [5..300]: ", "d")
    L = get_valid_input("Длина вала L, мм [10..3000]: ", "L")
    results = calculate_torsion(T, d, L, tau_allow)
    print("\n" + "-"*40)
    print("РЕЗУЛЬТАТЫ РАСЧЁТА:")
    print(f"Материал:               {material_name}")
    print(f"Касательное напряжение: {results['tau']:.2f} МПа")
    print(f"Допустимое напряжение:  {results['tau_allow']} МПа")
    print(f"Коэфф. использования:   {results['ratio']:.3f}")
    print(f"Угол закручивания:      {results['phi_rad']:.6f} рад ({results['phi_deg']:.4f}°)")
    print(f"Класс нагрузки:         {results['status']}")
    print("-"*40)
    if results['status'] == "Недопустимо":
        print("ВНИМАНИЕ: Условие прочности не выполняется (τ > [τ])!")
   

