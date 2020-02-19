import os
#dir(os) 
#for i in dir(os):
 #   if 'dir' in i:
  #      print(i)
#print[i for i in]
#os.mkdr("hello")
#os.rmdir("hii")
#os.listdir("hiii")
#file handlng
open("hii.txt","w")
f=open("hii.txt","w")
f.write("hello world")
f.close()
f=open("hii.txt","w")
f.write("hello amit")
f.read()
f.seek(0)
f.close()
f=open("hii.txt","r+")
f.write("/n hii every one")
f.raedline()
f.seek(0)
f.close()
f=open("hii.txt","w+")
f.write("hello amit")
f.raed()
f.seek(0)
f.read()
f.close()
f=open("hii.txt","a")
f.write("hello i am amit")
f.close()
f=open("hii.txt","a+")
f.write("hello  guys i am amit")
#file op....
import sys
file_names=sys.argv[1:]
for i in file_names:
    f=open(i,'w')
    f.write("hii guys")
    f.close()
    
#alternate ways
    for i in file_name:
        with open('w')as f:
            f.write("hii every one")
            
#like append file


