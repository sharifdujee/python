num = int(input("Enter a number to check it's prime or not"))
flag = False

if num == 0 or num == 1:
    print("the number is not prime")

elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(f"{num}the number is not prime")
    else:
        print(f"{num} is a prime number")


