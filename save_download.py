import json

def save(schedule, filename="schedule.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(schedule, f, ensure_ascii=False, indent=5)
    print(f"Расписание сохранено в файл {filename}")

def download(filename="schedule.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл с расписанием не найден. Будет использовано пустое расписание.")
        return {
            "Понедельник": [],
            "Вторник": [],
            "Среда": [],
            "Четверг": [],
            "Пятница": [],
            "Суббота": []
        }