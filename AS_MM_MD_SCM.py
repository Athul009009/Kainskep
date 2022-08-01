
from cgitb import text


class Acces_Specifiers:
    # Variouds oops lang control acess to objects 
    # most programming lang have 3 types of access modifers namely
                            # public 
                            # protected
                            # privete
    
    def public():
        # the decleard variables/objects are accesable from all part of the program 
        # all variables are public from default 
        class a:
            def __init__(self,name,age):
                self.aname=name
                self.aage=age
            
            def displayAge(self):
                print("age  :",self.aage)
                # public function and accessing public variables
        obj = a("athul",22)
        print("Name is  :",obj.aname)
        obj.displayAge()
    # public()
    
    # here name and age is public variables we can see that we can access it from outside the class "a"
    #  this is public access specifier 
    
    # class protected:
    #     # in here te decleared variables are only accesable from a class dirrived from it 
        #  use "__" symbol to reperesent protected "double underscore"
 
        class school:
            __name=None
            __age=None
            __rollno=None
            
            def __init__(self,name,age,rollno):
                self.__name=name
                self.__age=age
                self.__rollno=rollno
            def dis(self):
                print("roll :",self.__rollno)
                print("age  :",self.__age)
            
        class stu(school):
                    def __init__(self,name,age,rollno):
                            self.__name=name
                            self.__age=age
                            self.__rollno=rollno
                        
                    def dis(self,__name):
                                print("name :",self.__name)
                                self.dis()
                    dis("")
        obj=stu("athul",22,19)
        obj.dis()
                    
           
           
               
    class private:
                # here the decleared variables/objects are only accessable within the class 
                # it is considerd as one of the most secure modifiers amoung the three  
                
        class athul:
            __name=None
            __roll=None
            __branch=None
            
            def __init__(self,name,roll,branch):
                self.__name=name
                self.__roll=roll
                self.__branch=branch
                
            def __dis(self):
                print("name :",self.__name)
                print("roll_no :",self.__roll)
                print("branch :",self.__branch)
                
            def acess(self):
                
                self.__dis()
        
    # obj=athul("athul", 09 ,"cs")
    # obj.acess() 
                       



class Magic_Methods:
    
    #  dunder or magic methods in python are methords having 2 prefix or suffix underscores in methord name dunder here mean double under 
    
    # eg- __add__ , __len__ , __repr__ etc...
    
    # __init__ methords is the constructer (runs without calling)
    
    class string:
        def __init__(self,string):
            self.string=string
            
        def __repr__(self):
            return "object  :{}".format(self.string)
        
        def __add__(self,other):
            return self.string + other
        
    if __name__ == "__main__":
        string1 =string('hello')
        print(string1 + "athul")   
        

class method_decoraters:
    
    # decoraters is a very powerful and useful tool it allows the user to modifi the behaviour of a function
    
    # it allows to wrap a function into another function to extend the primery function
    
    # Functions are first class objects ther propertys are as follows 
    
                # a function is an inastence of the object type
                # you can store function in a variable
                # can pass function as a parameter 
                # you can store them in a data structure
                
        # example -
            def A(text):
                 return text.upper() # this accepts a text and turn it into uppercase 
             
            print(A("hello")) #print hellow in upper case
            
            x=A # FUNTION INTO VARIABLE "X"
            
            print(x("hello")) # using that variable we use the respective function
            
    # passing function as a argument
    
            def loud(text):
                return text.upper() # accepts a text and turn it into uppercase
            
            def slow(text):
                return text.lower() # accepts a text and turn it into lowercase
            
            def greet(fun):
                h=fun("Heey Boy ") # put function into a variable 
                print(h) 
                
            greet(loud)  # pass loud into greet amd print HELLO
            greet(slow)  # pass slow into greet amd print hello
            
    #  DECORATORS
    
        # manupulating certain function 
        # or
        # executing funtions within a function
        
            def def1(fun):
                def now():
                    print("heey its me !!")
                    fun()
                    print("who r u ?")
                return now
            
            def who():
                print("wait a min !!!!")
                
            who = def1(who) # from here onwords function who is not who it is passed as an argument to first function  
            who()  
            
            
            
class Static_class_methords:
    
    # CLASS METHOD 
    
    # class methord is a bultin function decorator that is an expression that get evaluated after your function is defined 
    
    # class methord is a method that is bount to the class and not the objects 
    
    # they have acces to the state of the class by checking the parameter that points the class 
    
    # it can modifi the class state which will change all the instene of the class
    
       
    # STATIC METHOD
    
    # its a method that is bound to the class not the object of the class 
    
    # this methord cant access or modifi the class state 
    
    #  implimentation -
    
    from datetime import date
    
    class per:
        def __init__(self,name,age):
            self.name=name
            self.age=age
            
        @classmethod   # classic methord decorator
        def birth(self,name,year):
            return self(name,date.today().year - year)
        
        @staticmethod       # static method decorator
        def adult(age):
            return age>18

    per1=per("athul",22)
    per2=per.birth("Athul",1999)
    
    print(per1.age)
    print(per2.age)
    print(per.adult(22))
    
