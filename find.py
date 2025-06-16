def find(current_schedule):
    class_name = input("Введите название занятия для поиска: ")
    f = False
    print(f"Поиск занятия '{class_name}':")
    for day, classes in current_schedule.items():
        for c in classes:
            count = [c.lower() for c in classes].count(class_name.lower())
            if count > 0:
                print(f" - {day} (встречается {count} раз(а))")
                f = True      
    if f == 0:
        print("Занятие не найдено в расписании.")
