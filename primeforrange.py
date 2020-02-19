num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
#num1=12
#num2=50
for value in range(num1,num2+1):
    if value>1:
        for n in range(2,value):
            if (value%n)==0:
                break
            else:
                print(value)