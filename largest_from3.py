import numbers


def fun1(number1, number2, number3):
    if (number1 + number2) > (number2 + number3):
        if number1 > number2:
            print("Number1 is largest: {}".format(number1))
        else:
            print("Number2 is largest: {}".format(number2))
    else:
        if number3 > number2:
            print("Number3 is largest: {}".format(number3))
        else:
            print("Number2 is largest: {}".format(number2))

def fun2(n1, n2, n3):
    if n1>=n2 and n1>=n3: 
        print(" n1 is greatest");
    if n2>=n1 and n2>=n3:
        print(" n2 is greatest");
    if n3>=n1 and n3>=n2:
        print("n3 is greatest");

number1 = input("Enter 1st number: ")
number2 = input("Enter 2nd number: ")
number3 = input("Enter 3rd number: ")

fun2(number1, number2, number3)