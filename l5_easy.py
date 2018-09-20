# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for a in range(9):
    if a <= 9:
         os.mkdir(f'dir_{int(a)+1}')
         a +=1

print("Folders were created!")

for i in os.listdir(path):
    name = os.path.join(path,i)
    if os.path.isdir(name) and "dir" in i:
         os.remove(name)

print("folders were deleted")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
"""Отображает только папки, без файлов"""

print([a for a in os.listdir() if not "." in a])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os

shutil.copyfile(__file__, os.path.join(os.curdir,"copy.py"))
print("Copy was created!")


#functions for normal

def create_folder(name_create):
    try:
        os.mkdir(name_create)
        print("Folder was created!")
    except:
        print("There is already such folder")

def delete_folder(name_delete):
    try:
        os.rmdir(name_delete)
        print("Folder was deleted")
    except:
        if os.path.exists(name_delete) == False:
            print("This folder does not exist")
        else:
            print("This folder has files, please, remove files first")
