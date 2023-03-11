def menu(data):
    menu_dict = {
        "1" : "Вывести справочник на экран",
        "2" : "Найти по фамилии",
        "3" : "Добавить запись",
        "4" : "Изменить запись",
        "5" : "Удалить запись",
        "6" : "Выйти"
        }
    print()
    for key, value in menu_dict.items():
        print(key, value)
    choice = input()
    if choice == "1":
        print_data(data)
    elif choice == "2":
        search_data(data)
    elif choice == "3":
        add_fio(data)
    elif choice == "4":
        change_data(data)
    elif choice == "5":
        delete_data(data)
    elif choice == "6":
        save_change = input("Сохранить изменения? y/n \n")
        if save_change == "y":
            write_data(data)
            print("Изменения сохранены")
        return False
    return True
    
def read_data():
    with open("fio.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

def write_data(data):
     with open("fio.txt", "w", encoding="utf-8") as file:
        data = file.writelines(data)

def print_data(data):
    print("\n")
    for i in range(len(data)):
        print(i, data[i].strip().replace(";", " "))
   
def add_fio(data):
    new_fio = list(input("Введите ФИО и номер телефона через пробел: ").split())
    new_record = []
    for elem in new_fio:
        new_record.append(elem)
    data.append("\n" + ';'.join(new_record))

def search_data(data):
    surname = input("Введите фамилию для поиска: ")
    for elem in data:
        if elem.find(surname) != -1:
            print("Найдена запись: " + elem.strip().replace(";", " "))
    

def change_data(data):
    change_index = int(input("Введите номер записи, которую хотите изменить: "))
    print("\nМеняется запись: " + data[change_index].strip().replace(";", " "))
    change_fio = list(input("Введите измененную запись: ").split())
    new_record = []
    for elem in change_fio:
        new_record.append(elem)
    data[change_index] = ';'.join(new_record) + "\n"
    print("Запись изменена")

def delete_data(data):
    del_choice = int(input("Введите номер записи, которую хотите удалить: "))
    print("\nСтрока " + data.pop(del_choice) + " удалена")

def main():
    data = read_data()
    while menu(data):
        continue
if __name__ == "__main__":
    main()