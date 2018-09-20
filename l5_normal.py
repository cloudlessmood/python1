# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os

try:
    a = int(input("Write the number of the action you want to: "
              "1.Move to the folder; "
              "2.Look at the folder contents;"
              "3.Delete folder;"
              "4.Create folder - "))
    if a == 1:
        name_move = input("I did not understand the task for this part :)")

    elif a == 2:
        print(os.listdir())

    elif a == 3:
        from l5_easy import delete_folder
        name_delete = input("Write the name of the folder: ")
        l5_easy.delete_folder(name_delete)

    elif a == 4:
        from l5_easy import create_folder
        name_create = input("write the name of the folder: ")
        l5_easy.create_folder(name_create)

    else:
        if a>4 or a ==0:
            print("You put the wrong number!")

except:
    print("it is not the number")