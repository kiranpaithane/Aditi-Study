'''
 dictionary is the combination of key value pair.
 in which key is always unique, but values are not unique.

 key is of immutable type means we can not change it.

 '''


data = { 1:'kiran', 2:'athang', 3:'shreays', 4:'vishal' }
print(data)

# to fetch the value we use key to fetch it.

print( data[3] )

# another way to fetch value id using in built get function

print(data.get(5))      # if the key is not present get will give "None" as a result

# if key not present
print(data.get(5, "key not present"))














'''



# we can merge to lists as a dictionary


keys = ['kiran', 'athang', 'shreyas']
values = ['python', 'cpp', 'JS'] 

result = dict( zip(keys,values) )               # this function will create dictionary of two lists
                                                # {'kiran': 'python', 'athang': 'cpp', 'shreyas': 'JS'}
print(result)


# if we have to add new entery in dictionary we have to use

result ['vishal'] = 'java'

print(result)






















# to delete the entry from dictionry use 'del' function

del result ['vishal']
print(result)

'''




