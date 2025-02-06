num_list = [1, -2, 0, 3, -5, 0]

num_dic = {
    "positive": list(filter(lambda x: x > 0, num_list)),
    "negative": list(filter(lambda x: x < 0, num_list)),
    "zero": list(filter(lambda x: x == 0, num_list))
}

print(num_dic)