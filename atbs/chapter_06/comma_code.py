def comma_code(array):

    if len(array) == 0:
        return ""
    if len(array) == 1:
        return array[0]

    output = ""
    last_val = str(array.pop())

    for i, val in enumerate(array):
        output += str(val) + ', '

    output += 'and ' + last_val

    return output

print(comma_code([1, 2, 3]))
print(comma_code([1, 2]))
print(comma_code([1]))
print(comma_code([]))

print(comma_code(['red', 'blue', 'green']))