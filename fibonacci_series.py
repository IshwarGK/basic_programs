import numbers


def fun1(number):
    first = 0
    second = 1
    result = 1
    for i in range(number):
        if i < 2:
            print(i)
        else:
            result = first + second
            first = second
            second = result
            print(result)

number = input("Enter the Number: ")
fun1(number)