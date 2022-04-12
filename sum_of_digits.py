def sum_fun(num):
    if num <= 1:
        return num
    return (num % 10) + sum_fun(num // 10)

num = input("Enter the Number: ")
print(sum_fun(num))