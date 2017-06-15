
# coding: utf-8

# In[1]:

word = 'lead'


# In[2]:

for char in word:
    print(char)


# In[7]:

elements = ['oxygen', 'nitrogen', 'argon']
for char in elements: # char is a variable
    print(char)


# In[8]:

for banana in word:
    print(banana)


# In[9]:

letter = 'z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is', letter)


# In[10]:

print(len('aeiou'))


# ## From 1 to N

# In[17]:

print(range(3))


# In[18]:

for num in range(3, 10, 3):
    print(num)


# In[19]:

5 ** 3


# In[20]:

result = 1
for i in range(0, 3):
    result *= 5
print(result)


# In[27]:

str = 'Newton'
str1 = 'Newton'


# In[28]:

print(str)
print(str1)


# In[30]:

for char in str1:
    print(char)


# In[33]:

# Reverse a String
newstring = ''
oldstring = 'Newton'
for char in oldstring:
    newstring += char
print(newstring)


# In[34]:

newstring = ''
oldstring = 'Newton'
for char in oldstring:
   newstring = char + newstring
print(newstring)


# ## Computing the Value of a Polynomial

# In[35]:

x = 5
cc = [2, 4, 3]


# In[36]:

y = cc[0] * (x ** 0) + cc[1] * (x ** 1) + cc[2] * (x ** 2)


# In[37]:

print(y)


# In[38]:

y = 0
for i, c in enumerate(cc):
    y = y + (x ** i) * c


# In[39]:

print(y)


# In[ ]:



