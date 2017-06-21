
# coding: utf-8

# In[1]:

whos%


# In[2]:

def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15


# In[3]:

fahr_to_kelvin(32)


# In[4]:

print(5 / 9)


# In[5]:

3 // 2 # Integer Division


# In[6]:

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))


# In[7]:

def fahr_to_celsius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celsius(temp_k)
    return result

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))


# In[8]:

def analyze(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

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


# In[9]:

def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')


# In[15]:

import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('data/inflammation*.csv')
print(filenames)

for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)


# ## Testign and Documenting

# In[16]:

def center(data, desired):
    return (data - numpy.mean(data)) + desired


# In[18]:

z = numpy.zeros((2, 2))
print(center(z, 3))


# In[20]:

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print(center(data, 0))


# In[21]:

print('original min, mean, and max are:', numpy.min(data), numpy.mean(data), numpy.max(data))
centered = center(data, 0)
print('min, mean, and max of centered data are:', numpy.min(centered), numpy.mean(centered), numpy.max(centered))


# In[22]:

print('std dev before and after:', numpy.std(data), numpy.std(centered))


# In[24]:

print('difference in standard deviations before and after:', numpy.std(data) - numpy.std(centered))


# ## Function Documentation

# In[25]:

def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.'''
    return (data - numpy.mean(data)) + desired


# In[26]:

help(center)


# In[27]:

def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + desired

help(center)


# In[28]:

def center(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + desired


# In[29]:

test_data = numpy.zeros((2, 2))
print(center(test_data, 3))


# In[30]:

more_data = 5 + numpy.zeros((2, 2))
print('data before centering:')
print(more_data)
print('centered data:')
print(center(more_data))


# In[31]:

def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)


# In[32]:

help(numpy.loadtxt)


# In[33]:

def fence(original, wrapper):
    return wrapper + original + wrapper


# In[34]:

print(fence('name', '*'))


# In[37]:

def outer(original):
    return original[0] + original[-1]


# In[38]:

print(outer('helium'))


# ## Rescaling an Array

# In[40]:

def rescale(data):
    min_value = numpy.min(data)
    max_value = numpy.max(data)
    rescaled_data = (data - min_value) / (max_value - min_value)
    return rescaled_data


# In[41]:

rescale(data)


# In[42]:

help(numpy.arange)


# In[43]:

numpy.arange(10.0)


# In[44]:

rescale(numpy.arange(10.0))


# In[45]:

numpy.linspace(0, 100, 5)


# In[46]:

help(numpy.linspace)


# In[47]:

rescale(numpy.linspace(0, 100, 5))


# In[48]:

def rescale(input_array, low_val=0.0, high_val=1.0):
    '''rescales input array values to lie between low_val and high_val'''
    L = numpy.min(input_array)
    H = numpy.max(input_array)
    intermed_array = (input_array - L) / (H - L)
    output_array = intermed_array * (high_val - low_val) + low_val
    return output_array


# In[51]:

f = 0
k = 0

def f2k(f):
  k = ((f-32)*(5.0/9.0)) + 273.15
  return k

print(f2k(8))
print(f2k(41))
print(f2k(32))

print(k)


# In[52]:

def numbers(one, two=2, three, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n

print(numbers(1, three=3))


# In[53]:

def numbers(one, three, two=2, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n

print(numbers(1, three=3))


# In[54]:

def func(a, b=3, c=6):
  print('a: ', a, 'b: ', b, 'c:', c)

func(-1, 2)


# In[55]:

a = 3
b = 7

def swap(a, b):
    temp = a
    a = b
    b = temp

swap(a, b)

print(a, b)


# In[56]:

a, b = [b, a]


# In[57]:

print(a, b)


# In[58]:

a, b = b, a


# In[59]:

print(a, b)

