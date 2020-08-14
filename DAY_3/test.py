

'''

for i in range(4):                             # 0-3   1st time 1 , 2nd 2
    for j in range(i+1):   # 2 times                       # 0- 1+1 (2) 
        print("#", end=" ")   #
    print()


'''

for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()
