
# coding: utf-8

# # Analyzing Patient Data

# ## Assign a value to a variable

# In[1]:

weight_kg = 55


# In[2]:

print(weight_kg)


# In[3]:

print('weight in pounds:', 2.2 * weight_kg)


# In[4]:

weight_kg = 57.5
print('weight in kilograms is now:', weight_kg)


# In[5]:

weight_lb = 2.2 * weight_kg
print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)


# In[6]:

weight_kg = 100.0
print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)


# ## Who's Who in Memory

# In[7]:

get_ipython().magic('whos # view variables')


# ## Import 

# In[8]:

import numpy


# In[9]:

numpy.loadtxt(fname = 'data/inflammation-01.csv', delimiter = ',')


# In[10]:

get_ipython().magic('whos # commmand above did not save data into memory')


# In[11]:

data = numpy.loadtxt(fname = 'data/inflammation-01.csv', delimiter = ',')


# In[12]:

get_ipython().magic('whos')


# In[13]:

print(data)


# In[14]:

print(type(data))


# ## Data type

# In[15]:

print(data.dtype)


# In[16]:

print(data.shape) # rows, column


# In[17]:

print('first value in data:', data[0, 0])


# In[18]:

print('middle value in data:', data[30, 20])


# In[19]:

print(data[0 : 4, 0 : 10]) # select sections, up to but not including


# In[20]:

print(data[5 : 10, 0 : 10])


# In[21]:

small = data[: 3, 36 :]
print('small is:')
print(small)


# In[22]:

doubledata = data * 2.0


# In[23]:

print('original:')
print(data[: 3, 36 :])
print('doubledata:')
print(doubledata[: 3, 36 :])


# In[24]:

tripledata = doubledata + data


# In[25]:

print('tripledata:')
print(tripledata[: 3, 36 :])


# In[26]:

# average inflammation for all patients on all days
print(numpy.mean(data))


# ### Not All Funtions Have Input

# In[27]:

import time
print(time.ctime())


# ## Basic NumPy funtions

# In[32]:

maxval, minval, stdval = numpy.max(data), numpy.min(data), numpy.std(data)
print('maximum:', maxval)
print('minimum inflammation:', minval)
print('standard deviation:', stdval)


# In[113]:

get_ipython().magic('pinfo numpy.cumprod')


# When analyzing data, though, we often want to look at partial statistics, such as the maximum value per patient or the average value per day. One way to do this is to create a new temporary array of the data we want, then ask it to do the calculation:

# In[34]:

patient_0 = data[0, :] # 0 on the first axis, everything on the second
print('maximum inflammation for patient 0:', patient_0.max())


# In[35]:

# an easier way not to store partial data
print('maximum inflammation for patient 2:', numpy.max(data[2, :]))


# Most array functions allow us to specify the axis we want to work on.

# In[36]:

print(numpy.mean(data, axis = 0))


# In[42]:

print(numpy.mean(data, axis = 0).shape)


# In[43]:

print(numpy.mean(data, axis = 1))


# In[44]:

print(numpy.mean(data, axis = 1).shape)


# ## Visualization

# In[49]:

import matplotlib.pyplot
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()


# ## Some IPython Magic

# In[61]:

# % indicates an IPython magic function: a function that is only valid within the notebook environment.
get_ipython().magic('matplotlib inline')


# In[63]:

ave_inflammation = numpy.mean(data, axis = 0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()


# In[67]:

max_plot = matplotlib.pyplot.plot(numpy.max(data, axis = 0))
matplotlib.pyplot.show()


# In[66]:

min_plot = matplotlib.pyplot.plot(numpy.min(data, axis = 0))
matplotlib.pyplot.show()


# ### Group similar plots in a single figure using subplots

# In[69]:

import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname = 'data/inflammation-01.csv', delimiter = ',')
fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis = 0))

fig.tight_layout()
matplotlib.pyplot.show()


# In[71]:

get_ipython().magic('whos')


# ### Scientists Dislike Typing
# you can use the shortcut of a package

# In[72]:

import numpy as np


# In[73]:

get_ipython().magic('whos')


# ## Challenges

# In[74]:

first, second = 'Grace', 'Hopper'
third, fourth = second, first
print(third, fourth)


# In[75]:

element = 'oxygen'
print('first three:', element[0 : 3])
print('last three:', element[3 : 6])


# In[77]:

element[4 :]


# In[78]:

element[:]


# In[79]:

print(element[-1])
print(element[-2])


# In[80]:

print(element[1 : -1])


# In[84]:

data[3 : 3, 4 : 4]
print(data[3 : 3, 4 : 4])


# In[82]:

data[3 : 3, :]


# In[92]:

fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0))

axes3.set_ylabel('min')
axes3.set_ylim(0, 6)
axes3.plot(numpy.min(data, axis = 0))

fig.tight_layout()
matplotlib.pyplot.show()


# In[95]:

fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0), drawstyle = 'steps-mid')

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0), drawstyle = 'steps-mid')

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis = 0), drawstyle = 'steps-mid')

fig.tight_layout()
matplotlib.pyplot.show()


# In[98]:

std_inflammation = matplotlib.pyplot.plot(np.std(data, axis = 0))
matplotlib.pyplot.show()


# In[101]:

fig = matplotlib.pyplot.figure(figsize = (4.0, 10.0))

axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis = 0))

fig.tight_layout()
matplotlib.pyplot.show()


# ### Stacking Arrays

# In[103]:

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('A =')
print(A)

B = numpy.hstack([A, A])
print('B =')
print(B)

C = numpy.vstack([A, A])
print('C =')
print(C)


# In[105]:

print(A[:, 0])
print(A[:, : 1])


# In[106]:

D = np.hstack((A[:, : 1], A[:, -1 :]))
print('D =')
print(D)


# In[110]:

D = np.delete(A, 1, 1)
print(D)


# In[114]:

np.diff(data, axis = 1)


# In[116]:

print((np.diff(data, axis = 1)).shape)


# In[117]:

data


# In[118]:

np.max(numpy.diff(data, axis = 1), axis = 1)


# In[119]:

numpy.max(numpy.absolute(numpy.diff(data, axis = 1)), axis = 1)


# In[ ]:



