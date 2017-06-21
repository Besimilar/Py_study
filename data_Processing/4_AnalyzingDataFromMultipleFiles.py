
# coding: utf-8

# In[1]:

import glob


# In[2]:

print(glob.glob('data/inflammation*.csv'))


# In[4]:

import numpy


# In[9]:

import numpy as np
import matplotlib.pyplot

filenames = sorted(glob.glob('data/inflammation*.csv'))
filenames = filenames[0:3]
for f in filenames:
    print(f)
    
    data = np.loadtxt(fname = f, delimiter = ',')
    fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))
    
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()


# ## Plotting Differences

# In[10]:

import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('data/inflammation*.csv')

data0 = np.loadtxt(fname = filenames[0], delimiter = ',')
data1 = np.loadtxt(fname = filenames[1], delimiter = ',')

fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

matplotlib.pyplot.ylabel('Difference in average')
matplotlib.pyplot.plot(data0.mean(axis = 0) - data1.mean(axis = 0))

fig.tight_layout()
matplotlib.pyplot.show()


# ## Generate Composite Statistics

# Generate a dataset containing values averaged over all patients

# In[13]:

# filenames = glob.glob('data/inflammation-*.csv')
# composite_data = np.zeros((60, 40))
# for f in filenames:
#     # sum each new file's data into as it's read
# # and then divide the composite_data by number of samples
# composite_data /= len(filenames)

import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('data/inflammation*.csv')
composite_data = numpy.zeros((60,40))

for f in filenames:
    data = np.loadtxt(fname = f, delimiter = ',')
    composite_data += data
    
composite_data /= len(filenames)

fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(composite_data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(composite_data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(composite_data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()


# In[ ]:



