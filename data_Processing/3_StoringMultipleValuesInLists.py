
# coding: utf-8

# ## List

# In[1]:

odds = [1, 3, 5, 7]
print('odds are:', odds)


# In[2]:

for num in odds:
    print(num)


# Be careful when modifying data in place. If two variables refer to the same list, and you modify the list value, it will change for both variables!

# In[4]:

salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
mySalsa = salsa        # <-- mySalsa and salsa point to the *same* list data in memory
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', mySalsa)


# In[5]:

salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
mySalsa = list(salsa) # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', mySalsa)


# ## Nested Lists

# In[6]:

x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]


# In[7]:

print([x[0]])


# In[8]:

print(x[0][0])


# In[9]:

odds


# In[10]:

odds.append(11)


# In[11]:

print('odds after adding a value:', odds)


# In[12]:

del odds[0]


# In[13]:

print('odds after removing the firest element:', odds)


# In[16]:

odds.reverse()
print('odds after reversing:', odds)


# # Challenge

# In[17]:

my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)


# In[18]:

string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"], ["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]


# In[20]:

string_for_slicing[-4 :]


# In[21]:

list_for_slicing[-4 :]


# In[22]:

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print("subset", subset)


# In[23]:

beatles = "In an octopus's garden in the shade"


# In[24]:

beatles[: : 2]


# ## Swapping the contents of variables

# In[25]:

left = 'L'
right = 'R'
left, right = [right, left]


# In[26]:

print(left, right)


# ## Overloading

# In[27]:

counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)


# In[28]:

print(counts + counts)


# In[ ]:



