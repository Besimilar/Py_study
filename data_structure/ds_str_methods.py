# @author Hongwei
# This is a string object
name = 'Hongwei'

if name.startswith('Hon'):
    print('Yes, the string starts with "Hon"')

if 'o' in name:
    print('Yes, it contains the string "a"')

if name.find('wei') != -1:
    print('Yes, it contains the string "wei"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', "India", "China"]
print(delimiter.join(mylist))
