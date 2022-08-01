# class and object

# almost all elements in python is an object 
# class is a container that holds the objects it divides the objects according to users preference

class NewClass:
    x1=int(input("ENETR THE FIRST NO :"))
    x2=int(input("ENETR THE SECOND NO :"))
    sum=x1+x2
# class syntax is as shown abow

# creation of objects on the basis of Newclass !!

q1=NewClass()
print(q1.sum)

# advantage of objects is that we can target the specific variable we want
# here its sum

# And there is the constructor 
# syntax is __init__()
# the advantage of this constructor is that its automatically called every time

class animal:
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age

animal1 = animal("dog",3)

print(animal1.breed)
print(animal.age)

# as shown there is no need for calling the function

#  self is used to represent the instences of the class and used to acces the variables that belong to the class 

#  it shoulldint nesserly be self we can name it as we want 

#  we can modifi obj propertys like " animal1.age=4 " 
# or
# if we want to delete the objects then " del animal1.age "

#  we can create new empty class using pass

class A:
    pass

# no error no output



