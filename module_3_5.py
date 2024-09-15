def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if int(str_number[:-1]) != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:

    else:
        return first

result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(3)
print(result2)
result3 = get_multiplied_digits(330)
print(result3)
result4 = get_multiplied_digits(0)
print(result4)