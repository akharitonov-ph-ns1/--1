import json

from display import screen
from check import check
from add import add
from delete import delete
from clear import clear_day
from clear import clear_full
from find import find
from save_download import save
from save_download import download

schedule = {
    "Понедельник": [],
    "Вторник": [],
    "Среда": [],
    "Четверг": [],
    "Пятница": [],
    "Суббота": []
}

def main():
    schedule = download()
    while True:
        print('')
        print("Меню: ")
        print("")
        print("1. Показать расписание")
        print("2. Добавить занятие")
        print("3. Удалить занятие")
        print("4. Очистить расписание на день")
        print("5. Очистить расписание полностью и создать новое")
        print("6. Поиск занятия в расписании")
        print("0. Выход и сохранение")
        print("")
        choice = input("Выберите действие (0-6): ")
        if choice == '1':
            screen(schedule)
        elif choice == '2':
            add(schedule)
        elif choice == '3':
            delete(schedule)
        elif choice == '4':
            clear_day(schedule)
        elif choice == '5':
            clear_full(schedule)
        elif choice == '6':
            find(schedule)
        elif choice == '0':
            save(schedule)
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Выберите от 0 до 6.") 
            
if __name__ == "__main__":
    main()
