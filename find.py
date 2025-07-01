from sort_bin_search import sort_schedule
from sort_bin_search import binary_search

def find(schedule):
    class_name = input("Введите название занятия для поиска: ").strip()
    if not class_name:
        print("Ошибка: пожалуйста, введите название занятия.")
        return
    sort_schedule(schedule)
    found_days = []
    for day, classes in schedule.items():
        indices = binary_search(classes, class_name)
        if indices:
            found_days.append((day, len(indices)))

    if found_days:
        print(f"\nЗанятие '{class_name}' найдено:")
        for day, count in found_days:
            print(f"- {day} (встречается {count} раз(а))")
    else:
        print("\nЗанятие не найдено в расписании.")
