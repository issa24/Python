#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Write a program that finds only numbers that are divisible by 7 
# but not multiple of 5 between 2000 and 3200.
num = list()
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        num.append(i)
        print(i,end=',')    
    


# In[27]:


# Write a program that accepts first and last name of a user and 
# prints in reverse.
fname = input('')
lname = input ('')
f = fname + ' ' + lname
print(f[::-1])


# In[34]:


import math
from math import pi
# Write a Python program to find the volume of a sphere with diameter 12 cm
r = 12 / 2
vol = 4/3 * pi * r**3
print(round(vol, 2))


# In[52]:


# Write a program that accepts a sequence of comma-separated numbers from
# console and generate a list.
inputs = input()
for items in inputs: 
    items = list()
    items.append(inputs)
    
print(items)


# In[202]:


# Create the below pattern using nested for loop in Python.
num = 5
for i in range(0, num):
    for p in range(0, i + 1):
        print("*", end=' ')
    print('')    
for i in range(num, 0, -1):
    for p in range(0, i - 1):
        print("*", end=' ')
         
    print('')       
    
    
        
           
        
    
   


# In[73]:


# Write a Python program to reverse a word after accepting the input from the
# user
userInput = input('')
reverseInput =  userInput[::-1]
print(reverseInput)


# In[99]:


# Write a Python program to print the given string in the format specified
# in the sample output
constituition = " WE, THE PEOPLE OF INDIA\n\thaving solemnly resolved to constitute India into a SOVEREIGN,!\n \t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n \t\t and to secure to all its citizens "

print(constituition)

