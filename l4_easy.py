# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

l = input("write list of any numbers separated by comma:").split(',')
new_l = [int(a)**2 for a in l]

print ("New list: ", new_l)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['apple', 'banana', 'grapefruit', 'peach']
fruits2 = ['peach', 'watermelon', 'banana', 'blackberry']

fruits = [a for a in fruits1 if a in fruits2]

print("first list:", fruits1)
print("second list:", fruits2)
print("fruits in botn", fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

l = [1,5,2,6,4,8,3,7,12,15]
l_new = [a for a in l if int(a)%3 == 0 and a>0 and int(a)%4 != 0]

print("original list: ", l)
print("new list:", l_new)