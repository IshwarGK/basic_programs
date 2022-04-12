def fun1(num):
    prime_number_list = []
    for i in range(1, num):
        count1 = 1
        for j in range(2, i/2+1):
            if i % j == 0:
                break
        else:
            prime_number_list.append(i)
    print(prime_number_list)

number = int(input("Enter the Number: "))
fun1(number)