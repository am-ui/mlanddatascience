from matplotlib import pyplot as plt
x=[2,5,3]
print(x)
 
 #Plotting to our canvas
plt.plot (x) 
plt.plot('info')
plt.ylabel('y')
plt.xlabel('x')
 #Showing what we plotted
  
plt.show()
#ploting of two curve
#input the data
x = [5,2,7]
y = [2,16,4]
#plot the x and y
plt.plot(x,y)
#set the title
plt.title('Info')
#set the labels
plt.ylabel('Y axis')
plt.xlabel('X axis')
#plot the graph
plt.show()
#import the matplotlib for varioous style
from matplotlib import style
 #use gg plot
style.use('ggplot')
#input the data
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
#set the labels and bandwidth
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
#set the title
plt.title('Epic Info')
#set the labels
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
#set the colors
plt.grid(True,color='k')
#show the graph
plt.show()
#plot the bar chart
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()
#plot the histogram 

#input the data
population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 #plot the scatter plot
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Scatter Plot')
plt.legend()
plt.show()
#plot the scatter plot with the help of slice plot
days = [1,2,3,4,5]
 
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
 #plot the pie plot
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()
#plot the sub plot


#impport the numpy
import numpy as np
#define the unction
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
#arrange the number
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
#plot the sub plot
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()