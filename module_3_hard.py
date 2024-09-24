data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum = 0
new_list = []

for i in data_structure:
    if isinstance(i, list):
        calculate_structure_sum += sum(i)
    elif isinstance(i, dict):
        for key1 in i.keys():
            calculate_structure_sum += len(key1)
        calculate_structure_sum += sum(i.values())
    elif isinstance(i, tuple):
        for j in i:
            if isinstance(j, int):
                calculate_structure_sum += j
            elif isinstance(j, dict):
                for key2 in j.keys():
                    calculate_structure_sum += len(key2)
                calculate_structure_sum += sum(j.values())
            elif isinstance(j, list):
                for k in j:
                    for k2 in k:
                        for k3 in k2:
                            if isinstance(k3, tuple):
                                for k4 in k3:
                                    if isinstance(k4, int):
                                        calculate_structure_sum += k4
                                    elif isinstance(k4, str):
                                        calculate_structure_sum += len(k4)
                            elif isinstance(k3, int):
                                calculate_structure_sum += k3
                            elif isinstance(k3, str):
                                calculate_structure_sum += len(k3)
    elif isinstance(i, str):
        calculate_structure_sum += len(i)

print('Сумма', calculate_structure_sum)