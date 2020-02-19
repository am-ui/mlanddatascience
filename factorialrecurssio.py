def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=int(input("Enter the number"))
if num<0:
    print("please enter a positive number")
elif num==0:
    print("factorial of 0 is 1")
else:
    print("the factorial of",num,"is",recur_factorial(num))