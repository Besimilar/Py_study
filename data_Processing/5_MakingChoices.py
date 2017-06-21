
# coding: utf-8

# In[1]:

num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')


# In[2]:

num = -3

if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")


# In[3]:

if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')


# In[5]:

if (1 > 0) & (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')


# In[6]:

if (1 < 0) or (-1 < 0):
    print('at least one test is true')


# In[7]:

if (1 < 0) | (-1 < 0):
    print('at least one test is true')


# In[13]:

import numpy
import numpy as np
data = np.loadtxt(fname = "data/inflammation-01.csv", delimiter = ",")


# In[14]:

if numpy.max(data, axis = 0)[0] == 0 and numpy.max(data, axis = 0)[20] == 20:
    print('Suspicious looking maxima!')


# In[17]:

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')


# In[18]:

data = numpy.loadtxt(fname='data/inflammation-03.csv', delimiter=',')
if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')


# In[19]:

if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')


# In[20]:

if not '':
    print('empty string is not true')
if not 'word':
    print('word is not true')
if not not True:
    print('not not True is true')


# In[21]:

a = 1
b = 10

if a < b * 0.1:
    print("TRUE")
else:
    print("FALSE")


# In[22]:

print(abs(a - b) < 0.1 * abs(b))


# In[23]:

positive_sum = 0
negative_sum = 0
test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
for num in test_list:
    if num > 0:
        positive_sum += num
    elif num == 0:
        pass
    else:
        negative_sum += num
print(positive_sum, negative_sum)


# In[24]:

files = ['inflammation-01.csv', 'myscript.py', 'inflammation-02.csv', 'small-01.csv', 'small-02.csv']
large_files = []
small_files = []
other_files = []

for file in files:
    if 'inflammation-' in file:
        large_files.append(file)
    elif 'small-' in file:
        small_files.append(file)
    else:
        other_files.append(file)
        
print(large_files)
print(small_files)
print(other_files)


# In[25]:

vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(count)
print("The number of vowels in this string is " + str(count))


# In[ ]:



