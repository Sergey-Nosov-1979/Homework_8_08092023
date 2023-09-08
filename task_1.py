'''
Задача №49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
функционал для изменения и удаления данных.
'''

import os, re
def phone_format(n):  
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]
def printData(data):  
    phoneBook = []
    splitLine = "=" * 50
    print(splitLine)
    print(" №  Фамилия         Имя           Номер Телефона")
    print(splitLine)
    personID = 1
    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "№": personID,
                "Фамилия": lastName,
                "Имя": name,
                "Телефон": phone_format(phone),
            }
        )
        personID += 1
    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} - {phone:<15}")
    print(splitLine)
def showContacts(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n-- нажмите клавишу Enter --")
def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию контактного лица: ") + ","
        res += input("Введите имя контактного лица: ") + ","
        res += input("Введите номер контактного лица: ")
        file.write(res + "\n")
    input("\nКонтакт был успешно добавлен!\n-- нажмите клавишу Enter --")
def findContact(fileName):  
    os.system("cls")
    target = input("Введите элемент контакта для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break
    if len(result) != 0:
        printData(result)
    else:
        print(f"Контакта с этим элементом нет '{target}'.")
    input("-- нажмите клавишу Enter --")
def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата в главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый телефон: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n-- нажмите клавишу Enter --")
        else:
            return
def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
        numberContact = int(
            input("Введите номер контакта для удаления или 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
        else:
            return
    input("-- нажмите клавишу Enter --")
def drawInterface():  
    print("#####   Телефонный справочник   #####")
    print("=" * 26)
    print(" 1 - Показать телефонный справочник")
    print(" 2 - Добавить контакт")
    print(" 3 - Найти контакт")
    print(" 4 - Изменить контакт")
    print(" 5 - Удалить контакт")
    print("\n 0 - Выход")
    print("=" * 26)
def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите номер от 1 до 5 или 0 для выхода: "))
        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо! До свидания.")
            return
path = "phonebook.txt"
main(path)