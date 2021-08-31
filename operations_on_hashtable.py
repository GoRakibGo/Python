#operrations on hashtable
my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
#accessing items
print(my_dict['Dave'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Ava'))
print('All the names :')
for x in my_dict:
    print(x)

print('All the values :')
for y in my_dict.values():
    print(y)

print('All the name and values :')
for z in my_dict.items():
    print(z)

#updating hashtable
my_dict['Dave'] = '004'
my_dict['Chris'] = '005'
print(my_dict)

#deleting entries
print(my_dict.pop('Ava'))
print(my_dict.popitem())
del my_dict['Dave']
print(my_dict)