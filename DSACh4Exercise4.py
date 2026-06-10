def gratest_number(array):
    if not array:
        return None
    greatest = 0
    for num in array:
        if num > greatest:
            greatest = num
    return greatest
print(gratest_number([10,50,1,55,78]))
