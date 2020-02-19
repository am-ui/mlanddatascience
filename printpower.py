num=11
number=int(input("Enter the number"))
result = list(map(lambda x: number** x, range(num)))
for i in range(num):
   print("2","*",i,"=",result[i])