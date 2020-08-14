# Set -: it is collection of unique elements
# we use curly bracket for set.
# set uses the concept of hash , it increases the performance

s = {10,35,14,75,64}
print(s)                       # {64, 35, 10, 75, 14}

# set never follows the sequence


s1 = {41,55,72,53,55,98}
print(s1)                       # {98, 72, 41, 53, 55}

# its not going to print repeating values

#print(s1[2])                 TypeError: 'set' object is not subscriptable means set does not support indexing