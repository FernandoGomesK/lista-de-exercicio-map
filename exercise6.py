num_list = [1, 2, 3, 4, 5, 6]


num_dic = {
    "even": list(filter(lambda x: x % 2 == 0, num_list)),
    "odd": list(filter(lambda x: x % 2 == 1, num_list))
}

print(num_dic)