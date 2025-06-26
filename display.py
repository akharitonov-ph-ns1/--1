def screen(current_schedule):
    print('')
    print("Текущее расписание: ")
    print('')
    for day, classes in current_schedule.items():
        if classes:
            print(f"{day}:")
            for i, class_name in enumerate(classes, 1):
                print(f" {i}. {class_name}")
        else:
            print(f"{day}: Нет занятий")
