#concate the two dataframe
#import pandas as pd

#df = pd.DataFrame({"A":["sofia", 5, 8, 11, 100],
 #                  "B":[2, 8, 77, 4, 11],
 #                  "C":["amy", 11, 4, 6, 9]})
#print(df)
#df2=pd.DataFrame({"D":["amit",7,9,4,7,5,10],
 #                 "E":["amzad",6,8,3,9,17,45],
  #                "F":["munna",45,67,87,98,776,78]})
#print(df2)
#am = pd.DataFrame(df,index=[0, 1, 2, 3])
#pa=pd.DataFrame(df2,index=[4,5,6])
#Frame=[df.df2]
#kon=pd.concat(Frame)
#merge the two dataframe for the different keys as x, y
#df3 = pd.DataFrame({"Name":["sofia","rahman","makhbool","radha","krishna"],
 #                  "address":["bihar","rajsathan","madhyapradesh","jharkhand","luckhnow"],
  #                 "salary":[10000,50000,70000,60000,55000]})
#df4=pd.DataFrame({"Name":["ayush","krishna","manish","manu"],
#                   "address":["ranchi","bihar","utarpradesh","jhanshi"],
 #                 "salary":["40000","60000","70000","80000"]})
#am2=pd.DataFrame(df3,index=[0,1,2,3])
#am4=pd.DataFrame(df4,index=[4,5,6,7])
#print(am2)
#print(am4)
#Frame[df3,df4]
#kon=pd.concat(Frame,key=['x','y'])
#print(kon)
#merge the two data farame  for different vakue
#df3 = pd.DataFrame({"Name":["sofia","rahman","makhbool","radha","krishna"],
 #                  "address":["bihar","rajsathan","madhyapradesh","jharkhand","luckhnow"],
 #                  "salary":[10000,50000,70000,60000,55000]})
#df4=pd.DataFrame({"employee status":["worker","software devloper","tester","data sciece"]})
#am5=pd.DataFrame(df3,index=[0,1,2,3])
#print(am5)
#res = pd.concat([df3,df4],index=1)
#print(res)
#df5=pd.DataFrame({"Name":["sofia","rahman","radha","krisha","meghna"],
 #                 "address":["bihar","jharkhand","nepal","bhootan","chaina"],
  #                "salary":[10000,56000,7674388,674658,677587,68575847]})
#df6=pd.DataFrame({"name":["suman","ashutosh","ranjan","sukesh","ajay"],
 #                 "address":["mashrakh","siwan","chhapra","patna","hazipur"],
  #                "salaray":[10887,35678574,6478748,46478734,4687463]})
#import pandas as pd

# making data frame from csv file
#data = pd.read_csv("diamond.csv", index_col ="Name")

# retrieving row by loc method
#first = data.loc["Avery Bradley"]
#second = data.loc["R.J. Hunter"]

#print(data)
#print(first, "\n\n\n", second)
# import pandas as pd
import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)