#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)# smtp session
s.starttls() # security
s.login("vvijaya594@gmail.com","xofnjyfkdtotxpnd")#sender mail.id
msg=input("enter ur message")
s.sendmail("vvijaya594@gmail.com","vijayaparlapalle0629@gmail.com",msg)
s.quit()


# In[ ]:




