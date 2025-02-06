name_list = ["Ana", "Lucas", "Fernanda", "João"]

more_five = list(filter(lambda x: len(x) >= 5, name_list))
print(more_five)