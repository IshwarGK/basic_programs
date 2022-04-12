def fun1(arr):
    arr_len = len(arr)
    for i in range(0, arr_len):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
                
    return arr

def bubble_sort(arr):
    len1 = len(arr) - 1

    for i in range(0, len1):
        swapped = False
        for j in range(0, len1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

    return arr

def selection_sort(arr):
    len1 = len(arr)
    for i in range(0, len1):
        min_val_index = i
        for j in range(i + 1, len1):
            if arr[min_val_index] > arr[j]:
                min_val_index = j
        if arr[i] > arr[min_val_index]:
            arr[i], arr[min_val_index] = arr[min_val_index], arr[i]

    return arr

arr = [89, 34, 12, 35, 88, 80, 32, 78]
arr1 = selection_sort(arr)
print(arr1)
