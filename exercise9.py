num_list = [(2, 8), (4, 5, 6), (1, 2), (20, 20)]

tuple_list = list(filter(lambda x: x >= 5, map(lambda x: sum(x) / len(x), num_list)))

print(tuple_list)