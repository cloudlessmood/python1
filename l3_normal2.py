import random
list = []

file = open("new.txt", "w")
for i in range(10):
    file.write(str(list.append(random.randint(-100,100))) + '\n')
file.close()

file = open('new.txt', 'w')
list1 = []
for a in file:
    if int(a)>0:
        list.append(a)

file.close()

print(file.read())