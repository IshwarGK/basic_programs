def fun1(number):
    count = number//2

    for i in range(2, count):
        if number % i == 0:
            print(i)
            print("Number is Not Prime")
            return

    print("Number is Prime")


number = input("Enter the number: ")
fun1(number)