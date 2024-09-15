def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    global recursion_level
    if len(str_number) > 1:
        recursion_level += 1
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0:
            if recursion_level == 0:
                return 0
            else:
                return 1
        else:
            return first


recursion_level = 0
result = get_multiplied_digits(402030)
print(result)