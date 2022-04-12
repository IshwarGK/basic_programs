def fun2(num, arr, l, r):
    mid = (1 + r - l)//2

    if arr[mid] == num:
        return mid
    elif num < arr[mid]:
        r = mid - 1
        fun2(num, arr, l, r)
    elif num > arr[mid]:
        l = mid + 1
        fun2(num, arr, l, r)
    elif l > r:
        return -1
    

def fun1(num, arr):
    len1 = len(arr)
    start = 0
    end = len1-1

    while len1:
        middle = (1 + (end - start))//2
        if num == arr[middle]:
            return middle
        elif num < arr[middle]:
            start = start
            end = middle - 1
        else:
            start = middle + 1
            end = end

        if start >= end:
            if arr[start] == num:
                return start
            return -1


arr = [1, 500, 900, 999]
num = 500
result = fun2(num, arr, 0, len(arr)-1)
print(result)