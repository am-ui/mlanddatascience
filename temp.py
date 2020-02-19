# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
       #bitwise and operator
in_num1=13
in_num2=15
print("input the number1:",in_num1)
print("input the nnumber2:",in_num2)
am=np.bitwise_and(in_num1,in_num2)
print("the bitwise operator is:",am)
in_arr=[1,2,3,4]
in_arr2=[6,3,4,3]
print("input the array1:",in_arr)
print("input the array2:",in_arr2)
am=np.bitwise_and(in_arr,in_arr2)
print("the bitwise operator:",am)
      #bitwise or operator
in_num1=13
in_num2=15
print("input the number1:",in_num1)
print("input the nnumber2:",in_num2)
am=np.bitwise_or(in_num1,in_num2)
print("the bitwise operator is:",am)
in_arr=[1,2,3,4]
in_arr2=[6,3,4,3]
print("input the array1:",in_arr)
print("input the array2:",in_arr2)
amit=np.bitwise_and(in_arr,in_arr2)
print("the bitwise operator:",amit)
      #bitwise operator xor
in_num1=13
in_num2=15
print("input the number1:",in_num1)
print("input the nnumber2:",in_num2)
am=np.bitwise_xor(in_num1,in_num2)
print("the bitwise operator is:",am)
in_arr=[1,2,3,4]
in_arr2=[6,3,4,3]
print("input the array1:",in_arr)
print("input the array2:",in_arr2)
amit=np.bitwise_xor(in_arr,in_arr2)
print("the bitwise operator:",amit)
      #bitwise invert
a=int(input("Enter the number"))
print(a)
x=np.invert(a)
print(x)
#left shift
a1=int(input("Enter the number first"))
print(a1)
bit_shift=int(input("Enter the number second"))
print(bit_shift)
y=np.left_shift(a1,bit_shift)#similarly right shift is accurs
print(y)
#biary repersetation
a1=int(input("Enter the number first"))
print(a1)
z=np.binary_repr(a1)
amit1=np.binary_repr(a1,width=5)#width method
print(amit1)
print(z)



