# Tuple is same as list, but tuple are immutable means we can not change value of tuple.
# it uses round brackets "()"
''' where we can use tuple?????
    whenever u have a list and u dont want to change the value of the list that time we can use tuple
    that's why iteration in tuple is faster
'''

# Example -:

tup = (10,35,14,75,64)
print(tup)

# to fetch value from tuple
print( tup[1] )



# try to repalace the value of tuple
#tup[2] = 50

'''
we get this error
 TypeError: 'tuple' object does not support item assignment
 
 '''
print (tup.count())