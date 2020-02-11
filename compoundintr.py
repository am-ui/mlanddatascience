def compound_interest():
    a=float(input("Enter the amount"))
    r=float(input("Enter the rate"))
    t=float(input("Enter the time"))
    CI=a*(pow(1+r/100),t)
    TA=CI+a
    print("totl compound interset:{}".format(CI))
    print("total amount amount:{}".format(TA))