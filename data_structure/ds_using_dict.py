# @author Hongwei
# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Hongwei': 'hu.hon@husky.neu.edu',
    'Similar': 'besimilar@gmail.com',
    'Besimilar': 'besimilar@sina.com',
    'Others': 'others@gmail.com'
}

print("Hongwei's address is", ab['Hongwei'])

# Deleting a key-value pair
del ab['Hongwei']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['News'] = 'news@gmail.com'

if 'News' in ab:
    print("\nGuido's address is ", ab['News'])
