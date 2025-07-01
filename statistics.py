def stat(current_schedule):
    print("Загруженность по дням:")
    for day, classes in current_schedule.items():
        if len(classes) > 1 and len(classes) < 5:
            print(f"{day}: {len(classes)} занятия")
        elif len(classes) == 1:
            print(f"{day}: 1 занятие")
        else:
            print(f"{day}: {len(classes)} занятий")
