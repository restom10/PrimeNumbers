#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factoresPrimos(n):
    x=2
    respuesta=""    
    while(n!=1):
        if(n%x==0):
            n=n/x
            respuesta+=" *"+str(x)
        else:
            x+=1
    return respuesta
            
    


# In[ ]:




