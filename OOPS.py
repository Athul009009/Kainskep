from soupsieve import select


class oops:
    # inheritence
    # inheritence helps in adding more features to a class without modifing it 
    # it provides reusability of code
    
    class person(object):
        def __init__(self,name):
            self.name=name
        def getName(self):
            return self.name
        def isEmployee(self):
            return False
    class employee(person):
        def isEmployee(self):
            return True
        
    emp=person("athul")
    print(emp.getName(),emp.isEmployee())
    emp=employee("dinesh")
    print(emp.getName(),emp.isEmployee())
    
    #  this is a great code to experiment the consepts of single level inheritence
    
    # multilevel inheritence
    # grandChild inherit Child and Child inherit Father
    
    class father(object):
        def __init__(self,name):
            self.name=name
        def name(self):
            return self.name

    class child(father):
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def age(self):
            return self.age
        
    class grandchild(child):
        def __init__(self,name,age,adress):
            self.name=name
            self.age=age
            self.adress=adress
            return self.adress
            
    # multiple inheritence
    # when child inherits more then one parents 
    
    class father(object):
        def __init__(self,name):
            self.name=name
        def name(self):
            return self.name

    class mother(object):
        def __init__(self,age):
            self.age=age
        def age(self):
            return self.age 
        
    class child(father,mother):
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def age(self):
            return self.age   
        
    # these are the most commenly used inheritences
    # besides this there is 2 more types they are Hirarchical , Hybrid inheritence
    
    # Hieraitance - more then one dirrived class from one parent
    # Hybrid - mix of 2 or more type of inheritence
    
    # polimorphism
    # polimorphism means having many forms in python it means same function name but different signatures/types
    
    # simple program 
    def sum(x,y,z=0):
        return x + y + z
    x1=sum(2,6)
    y1=sum(2,3,4)
    print(x1,y1)
    
    # polimorphisam using class
    
    class men:
        def intro(self):
            print("THERE ARE MANY TYPES OF MEN")
            
        def intel(self):
            print("Som men are intelligent some are Handsome")
            
    class intell(men):
        def intel(self):
            print("men are intelligent")
            
    class hands(men):
        def intel(self):
            print("men are handsome")
    
    obj_men=men()
    obj_itell=intell()
    obj_hands=hands()
    
    obj_men.intro()
    obj_men.intel()
    
    obj_itell.intro()
    obj_itell.intel()
    
    obj_hands.intro()
    obj_hands.intel()
    
# here we acess same methord with same same name on diffrent classes
# this is methord overriding
            
    # Abstaration 
    
# Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function

    class abstration:
        
        
      
        class Car(object):   
            def mileage(self):   
                pass  
        
        class Tesla(Car):   
            def mileage(self):   
                print("The mileage is 30kmph")   
        class Suzuki(Car):   
            def mileage(self):   
                print("The mileage is 25kmph ")   
        class Duster(Car):   
            def mileage(self):   
                print("The mileage is 24kmph ")   
        
        class Renault(Car):   
            def mileage(self):   
                    print("The mileage is 27kmph ")   
                
   
        t= Tesla ()   
        t.mileage()   
        
        r = Renault()   
        r.mileage()   
        
        s = Suzuki()   
        s.mileage()   
        d = Duster()   
        d.mileage() 
                
    
    
    
    