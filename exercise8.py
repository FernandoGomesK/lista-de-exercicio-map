from functools import reduce

word_list = ["casa", "python", "lambda"]

word_count = reduce(lambda x, y: x + y,map(lambda x: len(x), word_list))

print(word_count)