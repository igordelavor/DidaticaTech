#!/usr/bin/env python
# coding: utf-8

# In[2]:


#tupla é uma lista que não pode ser alterada, usa () na atribuição ao invés de []
tupla = (1,2,3)
tupla[0]


# In[10]:


#para transformar uma lista numa tupla
lista = [6,7,8]
print(lista)
novaTupla = tuple(lista)
print(novaTupla)


# In[11]:


type(lista)


# In[12]:


type(novaTupla)


# In[13]:


#para identificar como uma tupla precisa de pelo menos um numero e uma virgula
numero =(3)
type(numero)


# In[14]:


numero = (3,)
type(numero)


# In[ ]:




