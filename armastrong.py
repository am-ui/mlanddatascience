num1=float(input("Enter the number"))
if(num1==0):
    print("please Enter the positive number")
else:
    while (num1!=0):
        r=num1%10
        sum=r+pow(r,num1)
        num1=num1/10

    print("number is armstrong")
