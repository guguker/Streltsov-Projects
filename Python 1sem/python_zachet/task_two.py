def createDict(keys, values):
    
    result = {}

    for iter in range(len(keys)):

        if iter < len(values):
            result[keys[iter]] = values[iter]

        else:
            result[keys[iter]] = None
    
    return result


# Пример 1
keys = ['a1', 'b1', 'c1', 'd1']
values = [1, 11, 111]
print(createDict(keys, values))

# Пример 2
keys = ['a2', 'b2', 'c2']
values = [2, 22, 222, 2222]
print(createDict(keys, values))

# Пример 3
keys = ['a3', 'b3', 'c3', 'd3', 'e3']
values = [3, 0]
print(createDict(keys, values))
