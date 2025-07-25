def check(current_schedule, current_day, class_name):
    days_order = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    current_day_index = days_order.index(current_day)
    if current_day_index > 0 and current_day_index < 5:
        previous_day = days_order[current_day_index - 1]
        next_day = days_order[current_day_index + 1]
        if class_name in current_schedule[previous_day] or class_name in current_schedule[next_day]:
            return True
        else:
            return False
    elif current_day_index == 0:
        next_day = days_order[1]
        if class_name in current_schedule[next_day]:
            return True
        else:
            return False
    elif current_day_index == 5:
        previous_day = days_order[4]
        if class_name in current_schedule[previous_day]:
            return True
        else:
            return False
