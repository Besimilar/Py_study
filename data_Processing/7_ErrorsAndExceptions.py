
# coding: utf-8

# In[1]:

# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()


# ## Long Tracebacks
# Sometimes, you might see a traceback that is very long – sometimes they might even be 20 levels deep! This can make it seem like something horrible happened, but really it just means that your program called many functions before it ran into the error. Most of the time, you can just pay attention to the bottom-most level, which is the actual place where the error occurred.

# In[2]:

def some_function()
    msg = "hello, world!"
    print(msg)
     return msg


# In[3]:

def some_function():
    msg = "hello, world!"
    print(msg)
    return msg


# In[4]:

def some_function():
    msg = "hello, world!"
    print(msg)
    return msg


# In[6]:

count = 0
for number in range(10):
    count += number
print("The count is:", count)


# In[8]:

# This code has an intentional error. Do not type it directly;
# use it for reference to understand the error message below.
def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("friday")

print_friday_message()


# In[ ]:



