from functools import reduce

dic = {
    "João": [8, 7, 9], 
    "Ana": [5, 6, 7] 
}

average = {name: sum(x) / len(x) for name, x in dic.items()}


print(average)  