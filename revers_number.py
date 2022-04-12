import numbers


def fun1(number):
    number = str(number)
    len1 = len(number)
    len1 = len1 - 1
    result = ""
    for i in range(len1):
        index1 = len1 - i
        result = result + number[index1]
    result = result + number[0]
    print(result)

def fun2(number):
    revers = 0
    while number != 0:
        revers = revers * 10 + number % 10
        number = number // 10
    print(revers)

def fun3(number):
    str1 = str(number)
    revers = str1[::-1]
    print(revers)

number = input("input the number: ")
fun3(number)