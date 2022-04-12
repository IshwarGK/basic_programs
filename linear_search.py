def fun1():
    arr = [1, 4, 10, 2, 44, 889, 23, 90]
    count = 0
    for i in arr:
        if i == 55:
            return count
        count += 1

    return -1


print(fun1())