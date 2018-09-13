l = input("write list of numbers separated by comma: ").split(',')

def new_list(l):
    return(sum([int(i) ** 2 for i in l]))

print(new_list(l))