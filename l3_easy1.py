def new_number (number):
    count1 = int(count)
    number1 = number.split('.')
    left_part = number1[0]
    right_part = number1[1]

    last_number = int(right_part[count1-1])
    last1_number = int(right_part[count1])
    if last1_number >=5:
        last_number = last_number+1
    else:
        last_number

    right_new = right_part[:count1-1]+str(last_number)

    return ('{}.{}'.format(left_part, right_new))

number = input("write the number separates by the point: ")
count = input("write the count of values after point: ")

print(new_number(number))