def delete(current_schedule):
    day = input("Введите день недели (полностью): ")
    day = day.capitalize()
    if day in current_schedule:
        if current_schedule[day]:
            class_name = input("Введите название занятия для удаления: ")
            if class_name in current_schedule[day]:
                current_schedule[day].remove(class_name)
                print(f"Занятие '{class_name}' удалено с {day}.")
            else:
                print(f"Ошибка: занятие '{class_name}' не найдено в этот день.")
        else:
            print(f"В {day} нет занятий для удаления.")
    else:
        print("Ошибка: неверный день недели.")