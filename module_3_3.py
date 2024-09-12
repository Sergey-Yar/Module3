def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 3, 'поле']
values_dict = {'a': 'вжик', 'b': True, 'c': 55}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [333, 'poke']
print_params(*values_list_2, 42)