# break 

# in this case we will get only 5 chocolates, if requirment is of more than 5...


    

for i in range(0,101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)