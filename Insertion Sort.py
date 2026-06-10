def insertion_sort(array):
    for i in range(1, len(array)):
        temp_value = array[i]
        j = i - 1
        while j >= 0 :
            if array[j] > temp_value:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = temp_value
    return array
print(insertion_sort([55,27,88,45,78]))