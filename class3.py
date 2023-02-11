#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[1,2,3]
b=[4,5,6]
a.append(b)   ## this will give the ouput in the last postion with square bracket...
print(a)


# In[5]:


a=[1,2,3]
b=[4,5,6]
a.extend(b)
a.insert(1,b)
print(a)


# In[4]:


a=[1,2,3]
b=a
a.append(4)
print(a)
print(b)


# In[7]:


a=[1,2,3]
b=a.copy()
a.append(4)
print(a)
print(b)


# In[8]:


a=(1,2,3)
print(type(a))


# In[9]:


print(isinstance(a,tuple))


# In[13]:


print(max(a))
print(min(a))
print(sorted(a))
print(a.index(2))


# In[17]:


print(a.rindex(-2))


# In[15]:


print(a.find(2))


# In[18]:


##list is muteable
##tuple is nonmuteable.


# In[19]:


print a[0]


# In[20]:


a[0]


# In[21]:


a[::-1]


# In[22]:


##datatypes are int:numbers
##[]-list
##""-str
##()-tuple
##{}-set


# In[23]:


a={1,2,3}
print(type(a))


# In[24]:


a={1,1,1,2,2,2,3,3,3}
print(a)


# In[26]:


a=['hello','hello']
a=list(set(a))
print(a)


# In[27]:


a[0]


# In[29]:


a={1,2,3}
print(a[0]) ## in set indexing will not work...


# In[30]:


print(max(a))
print(min(a))
print(sorted(a))


# In[32]:


print(a.rindex(2))


# In[33]:


print(a.find(2))


# In[34]:


print(a.rfind(2))


# In[35]:


##in set datatype index,rindex,find,rfind nothing will not work in set...
##in tuple only index will work ..rindex,rfinf ,find will not work...


# In[37]:


a={1,2,3}
a.add(4)
print(a)


# In[42]:


a={1,10,20,3,4,100}
print(a.split("10"))


# In[43]:


##IMPNOTES SYNTAX FOR ALL DATATYPES COMMENTS..
##set is used to remove duplicate values...
##to find max no:print(max(a))
##to find type: print(type(a))
##to find min: print(min(a))
##to find sort: print(sorted(a))
##to find index: print(a.index("a"))
       ## rindex : print(a.rindex(""))
        ##same for find,rfind...
        ##for :append a.append()
        ##for :extend a.extend()
       ## for :count print(a.count(""))
       ## for :split print(a.split(""))
       ## for: replace print(a.replace(""))
       ## for: isinstance it is used to find true or false - print(isinstance(a,datatype like str,tuple,set,int,list))
       ## for: insert print(a.insert(position,value))...
       ## to :find whether input is alphabetic or not: print(a.isalpha()) ##it was used to find alphabetic..
           ## alphabetic and numerics : print(a.isalnum()) ##both alphabetic and numerics..
               ## to find digits : print(a.isdigit()) ## whether the input is digit or not
                    ## to find union numbers in both sets :print(a.union(b))
                     ##to find intersect numbers of both sets: print(a.intersect(b))       
                        ## to remove : print(a.remove()) it will remove the particular num
                        ## to del : a.del[] it will del the position...


# In[44]:


a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))


# In[45]:


print(a.intersection(b))


# In[46]:


print(a.difference(b))


# In[47]:


print(b.difference(a))


# In[50]:


a={1,2}
b={1,2,3,4}
print(a.issuperset(b))


# In[51]:


print(a.issubset(b))


# In[52]:


a={1,2,3}
b={3,4,5}
print(a-b)


# In[53]:


a=[1,2,3]
b=[4,5,6]
print(a+b)  ##it was a shortcut for extend...


# In[ ]:




