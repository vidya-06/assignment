#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-1

# In[1]:


x=5
y=(2*x+5)/(x**2+5*x+6)
print(y)


# In[2]:


x=5
y=(x**2+5*x+6)/(2*x+5)
print(y)


# In[8]:


x=int(input("enter x value"))
y=(2*x-3)*(x+9)
print(y)


# In[10]:


user='india'
password='ind123'


while(1):
    userinput=input("enter username:")
    userpassword=input("enter password:")



    
    if userinput=='india' and userpassword=='ind123' :
         print("congratulations login sucessful")
         break
    elif userinput=='india' and userpassword!='ind123' :
        print("incorrect password")
       
    else :
        print("incorrect credentials")


# In[ ]:




