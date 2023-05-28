#!/usr/bin/env python
# coding: utf-8

# # FACTORIAL OF A NUMBER

# In[5]:


number=int(input("enter any value"))
fact=1
while(number>0):
    fact=fact*number
    number=number-1
print("factorail=",fact)


# # NUMBER IS PRIME OR COMPOSITE

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


# # STRING IS PALINDROME OR NOT

# In[10]:


i=input("enter any string=")
j=i[-1::-1]
if(i==j):
    print("palindrome string")
else:
    print("not a palindrome string")


# # THIRD SIDE OF A RIGHT ANGLED TRIANGLE FROM TWO GIVEN SIDES

# In[11]:


from math import sqrt


# In[12]:


perpendicular=float(input("enter any value"))
base=float(input("enter any value"))
hypotenus=sqrt(perpendicular**2+base**2)
print(hypotenus)


# # FREQUENCY OF EACH CHARACTER GIVEN IN A STRING

# In[7]:


str=("Tom and Jerry")
count_dict={}
for i in str:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1
print("frequency of each character is=",(count_dict))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




