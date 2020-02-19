def print_factor(x):
    print("the factor of",x,"are")
    for i in range (1,x+1):
        if x%i==0:
            print(i)
    num=input("Enter the number")
    print(num)