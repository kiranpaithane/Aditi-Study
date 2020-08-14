'''
there are 2 types of errors.
1. Compile time error  (in python it are syntactical errors)
2. Logical error       (these errors by user)
3. run time error      (eg. divide by zero, error in database connection)

'''
 
a = 6
b = 3

try:
    print("db connection open")
    print(a/b)on
    

except Exception as e:
    print("runtime error is : ", e)
    

finally :
    print("db connection close")

    

