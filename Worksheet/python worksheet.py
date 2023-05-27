#!/usr/bin/env python
# coding: utf-8

# In[1]:


2+3


# In[2]:


A=34
B=45
C=A+B
C


# In[3]:


A=int(input("enter any value"))
B=int(input("enter any value"))
C=A+B
print(C)


# In[4]:


length=int(input("enter any value"))
breadth=int(input("enter any value"))
area=length*breadth
print(area)


# In[5]:


number=int(input("enter any value"))
fact=1
while(number>0):
    fact=fact*number
    number=number-1
print("factorail=",fact)


# In[7]:


num=int(input("enter any value"))
if num<=1:
    print(num,"composite number")
else:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is composite number")
            break
        else:
            print(num,"is prime number")


# In[10]:


i=input("enter any string=")
j=i[-1::-1]
if(i==j):
    print("palindrome string")
else:
    print("not a palindrome string")


# In[11]:


from math import sqrt


# In[12]:


perpendicular=float(input("enter any value"))
base=float(input("enter any value"))
hypotenus=sqrt(perpendicular**2+base**2)
print(hypotenus)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




