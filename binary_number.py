import numbers


def fun1(number):
    while number != 0:
        var1 = number % 10
        number = number // 10
        if var1 < 0 or var1 > 1:
            print("Number is not Binary")
            return
    print("Number is Binary")
    

number = input("Enter the number: ")
fun1(number)