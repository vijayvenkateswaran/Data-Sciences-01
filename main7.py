largest_number=None
for number in [4,56,18,78,23,99,12,203,156,14,32,199]:
    if largest_number is None:
        largest_number = number
    elif number > largest_number:
        largest_number = number
    print('This is in the set ',number,'and this is the largest number ',largest_number)
number = 55

number = int(number/3)
print(number)
number = float(55/3)
print(number)
print(type(number))
exit()
