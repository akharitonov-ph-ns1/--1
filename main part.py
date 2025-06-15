from display import screen
from check import check
from add import add
from delete import delete
from clear import clear_day
from clear import clear_full

schedule = {
    "Понедельник": [],
    "Вторник": [],
    "Среда": [],
    "Четверг": [],
    "Пятница": [],
    "Суббота": [],
    "Воскресенье": []
}

def func():
    while True:
        print('')
        print("Меню: ")
        print("")
        print("1. Показать расписание")
        print("2. Добавить расписание")
        print("3. Удалить занятие")
        print("4. Очистить расписание на день")
        print("5. Очистить расписание полностью и создать новое")
        print("0. Выход")
        print("")
        choice = input("Выберите действие (0-5): ")
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
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Выберите от 0 до 5.")
            
            
if __name__ == "__main__":
    func()