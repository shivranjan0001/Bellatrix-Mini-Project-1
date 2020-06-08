#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[6]:


#Calculator
#Bellatrix Mini Project 1
class Add():
    def add(self):
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a+b
        print("Addition of {} and {} is : ".format(a,b),c)
class Sub():
    def sub(self):
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a-b
        print("Subtraction of {} and {} is : ".format(a,b),c)
class Mul():
    def mul(self):
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a*b
        print("Multiplication of {} and {} is : ".format(a,b),c)
class Mod():
    def mod(self):
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a%b
        print("Modulation of {} and {} is : ".format(a,b),c)
class Per():
    def per(self):
        a=int(input('Enter the number that you have scored'))
        b=int(input('Enter the Total numbers'))
        c=(a/b)*100
        print("Persentage of that you have scored is : ".format(a,b),c)
class Div(Add,Sub,Mul,Mod,Per):
    def div(self):
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a/b
        print("Division of {} and {} is : ".format(a,b),c)
a=Div()
a.add()
a.sub()
a.mul()
a.div()
a.mod()
a.per()


# In[ ]:




