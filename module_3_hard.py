
def calculate_structure_sum(*args):
    summ = 0
    if not args:
        return 0
    else:
        for i in args:
            if isinstance(i, int):
                summ += i
                return summ
            elif isinstance(i, str):
                summ += len(i)
                return summ
            elif isinstance(i, list):
                calculate_structure_sum(i)
            elif isinstance(i, dict):
                for key in i.keys():
                    summ += len(key)
                    return summ
                for value in i.values():
                    summ += value
                    return summ
            elif isinstance(i, tuple):
                calculate_structure_sum(i)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('Сумма', calculate_structure_sum(data_structure))