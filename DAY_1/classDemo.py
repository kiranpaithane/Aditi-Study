class Parrot:

    # class attribute
    species = "bird"
    

    # instance attribute    
    # parameterize constructor              # whenever you create object/inctance 
    def __init__(self, name, age):   #name and age is parameter
        self.name = name
        self.age = age
    

     
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.age, blu.name))
print("{} is {} years old".format( woo.name, woo.age))