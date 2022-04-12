def swap_two_numbers(num1, num2):
    num2 = num1 + num2
    num1 = num2 - num1
    num2 = num2 - num1
    print("Num1: {}".format(num1))
    print("Num2: {}".format(num2))


def swap_two_numbers2(num1, num2):
    num1, num2 = num2, num1
    print("Num1: {}".format(num1))
    print("Num2: {}".format(num2))


num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")

swap_two_numbers2(num1, num2)
