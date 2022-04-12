import numbers


def fun1(number):
    sum = 0
    number1 = number
    while number1 != 0:
        number2 = number1 % 10
        sum = sum + fun_cub(number2)
        number1 = number1 // 10

    if sum == number:
        print("Number is Amstrong")
    else:
        print("Number is not Amstrong")

def fun_cub(number):
    return number * number * number


number = input("Enter the number: ")
fun1(number)