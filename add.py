from check import check

def add(current_schedule):
    day = input("Введите день недели (полностью): ")
    day = day.capitalize()
    if day in current_schedule:
        class_name = input("Введите название занятия: ").strip()
        if class_name == "":
            print("Ошибка. Введите название урока.")
            return
        else:
            if not check(current_schedule, day, class_name):
                current_schedule[day].append(class_name)
                print(f"Занятие '{class_name}' добавлено на {day}.")
            else:
                print(f"Ошибка: Занятие '{class_name}' уже было вчера.")
    else:
        print("Неверно введён день недели. Пожалуйста, исправьте ошибку и введите заново.")
