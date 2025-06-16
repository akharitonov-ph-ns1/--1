def check(current_schedule, current_day, class_name):
    days_order = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    current_day_index = days_order.index(current_day)
    if current_day_index > 0 and current_day_index < 6:
        previous_day = days_order[current_day_index - 1]
        next_day = days_order[current_day_index + 1]
        if class_name in current_schedule[previous_day] or class_name in current_schedule[next_day]:
            return True
        else:
            return False
