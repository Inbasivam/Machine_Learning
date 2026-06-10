def bubble_sort(arr):
    index=len(arr)-1
    sort = False
    while not sort:
        sort = True
        for i in range(index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort = False
        index-=1
    return arr
print(bubble_sort([5,4,3,2,1]))