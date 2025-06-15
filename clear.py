def clear_day(current_schedule):
    day = input("Введите день недели для очистки (полностью): ")
    day = day.capitalize()
    if day in current_schedule:
        if current_schedule[day]:
            current_schedule[day].clear()
            print(f"Все занятия на {day} удалены.")
        else:
            print(f"В {day} уже нет занятий.")
    else:
        print("Ошибка: Неверный день недели.")
        
def clear_full(current_schedule):
        for day in current_schedule:
            current_schedule[day].clear()
        print("Расписание очищено.")