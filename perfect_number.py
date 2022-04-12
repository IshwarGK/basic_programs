def perfect_number(num):
    sum = 1
    for i in range(2, (num/2 + 1)):
        if num % i == 0:
            sum = sum + i
    print(sum)
    if num == sum:
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")

num = input("Enter the Number: ")
perfect_number(num)
