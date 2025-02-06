from functools import reduce

num_list = [1, 2, 3, 4]
sum_num = reduce(lambda x, y: x + y, num_list)
print(sum_num)