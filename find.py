def find(current_schedule):
    class_name = input("Введите название занятия для поиска: ")
    f = False
    print(f"Поиск занятия '{class_name}':")
    for day, classes in current_schedule.items():
        for c in classes:
            if c.lower() == class_name.lower():
                print(f" - {day}")
                f = True
    if not f:
        print("Занятие не найдено.")
