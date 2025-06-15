def screen(current_schedule):
    print("Текущее расписание: ")
    for day, classes in current_schedule.items():
        if classes:
            print(f"{day}: {', '.join(classes)}")
        else:
            print(f"{day}: Нет занятий")