num=int(input("Enter a number"))

if num<0:
    print("Enter the positive number")

else:
    while(num<0):
        sum=0
        sum +=sum
        num -=1
    print("The sum is",sum)