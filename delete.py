def delete(current_schedule):
    day = input("Введите день недели (полностью): ")
    day = day.capitalize()
    if day in current_schedule:
        if current_schedule[day]:
            print(f"\nЗанятия на {day}:")
            for i, class_name in enumerate(current_schedule[day], 1):
                print(f"{i}. {class_name}")
            number_str = input("Введите номер занятия для удаления: ")

            if not number_str.isdigit():
                print("Ошибка: введите целое число.")
                return
            number = int(number_str)
            if number < 1 or number > len(current_schedule[day]):
                print("Ошибка: неверный номер занятия.")
                return

            removed_class = current_schedule[day].pop(number - 1)
            print(f"Занятие '{removed_class}' удалено с {day}.")
        else:
            print(f"В {day} нет занятий для удаления.")
    else:
        print("Ошибка: неверный день недели.")
