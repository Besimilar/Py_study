
# coding: utf-8

# ## Assertions

# In[1]:

numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n > 0.0, 'Data should only contain positive values'
    total += n
print('total is:', total)


# ## Broadly speaking, assertions fall into three categories:
# 
# * A precondition is something that must be true at the start of a function in order for it to work correctly.
# 
# * A postcondition is something that the function guarantees is true when it finishes.
# 
# * An invariant is something that is always true at a particular point inside a piece of code.

# In[5]:

def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dy) / dx
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)


# In[3]:

print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) ))


# In[6]:

print(normalize_rectangle( (0.0, 4.0, 2.0, 5.0) ))


# ## Test-Driven Development

# In[7]:

assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)


# In[37]:

def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    lowest = 0.0
    highest = 1.0
    for (low, high) in ranges:
        lowest = max(lowest, low)
        highest = min(highest, high)
    return (lowest, highest)


# In[35]:

def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)


# In[13]:

test_range_overlap()


# In[18]:

def get_total(values):
    assert len(values) > 0
    for element in values:
    	assert int(element)
    values = [int(element) for element in values]
    total = sum(values)
    assert total > 0
    return total


# In[19]:

get_total([1, 2, 3])


# In[20]:

values = [1, 2, 3]


# In[22]:

values = [str(element) for element in values]


# In[23]:

values


# In[27]:

values = [int(element) for element in values]


# In[28]:

values = [element + 5 for element in values]


# In[29]:

print(values)


# In[31]:

values + [5]


# In[32]:

values + [1, 2, 3, 4]


# In[40]:

import numpy

def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    if not ranges:
        # ranges is None or an empty list
        return None
    lowest, highest = ranges[0]
    for (low, high) in ranges[1:]:
        lowest = max(lowest, low)
        highest = min(highest, high)
    if lowest >= highest:  # no overlap
        return None
    else:
        return (lowest, highest)


# In[41]:

test_range_overlap()

