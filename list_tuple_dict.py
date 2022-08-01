from turtle import update


class list:
    # Python lists are like dynamically typed arrays in other languages
    # seperated by sq brackets [ ]
    def lst():
        v = ["athul","dinesh","c",100 ,199] #list contain multiple data types 
        print(v[0])
        # index based printing here in 0th index we have "athul" 
        # we can alo use negetive indexing like
        print(v[-1])  
        # list operations
    
    def input_list():
        str=input("enter elements   :")
        lst=str.split()
        print(lst)
        # using append we can also use insert into the list
        lst.append(3)
        print(lst)
        lst.reverse() # to reverse the list
    # input_list()
    
    def deletion_list():
        l1=[1,2,3,4,45,5,72,65,69]
        l1.remove(3)
        # it removes the element 3 from the list 
        l1.pop(4) # pop method can also be used for removal
        print(l1) #index based pop 
    # deletion_list()
    
    def slice():
        # we can slice list according to our needs 
        list=[1,2,3,4,5,6,7,8,9,0]
        print(f"initial list is :{list}")
        # sliceing elements 3 4 5
        l3=list[2:5]
        print(l3)
        
        l3=list[2:]  # here we slice from second index to full list 
        print(l3)
        
        # there is also negetive indexing eg - [-6:-4]
    # slice() 
    
    def comp():
        # list comprihention its more like a equation and the answers is listed in the respective list 
        # as example list of sq of all even nos under 10 in a list
        odd = [ x**2 for x in range(1,11) if x%2==0] 
        print(odd)
    # comp()
    
    # list methods
    
    # clear() - clear the list
    # sort() - sort the existing list in asending Order
    # extend() - add all elements of a list to another list
    # copy() - returns the copy of the list 
    
    
class tuple:
    # tuples are multiple items in a single variable 
    # tuple is immutable / unchangable 
    # tuple is also index based
    def tuple():
        t=("a","1",34)
        print(t)
    # tuple()
    
    def tuple_length():
        t=("apple","banana","pinapple","orenge")
        print(len(t))
        # it supports all data types int,strings,boolian etc..
        # it allows duplicate elements 
        # print(type(t))
        #  type mehord used to check the type of tuple 
        # tuple_length()
        # tuple also works on index basis
    def conversion_tuple():
        # to change a tuple u must change it into list and then edit then convert it back to tuple 
        a=("athul","c")
        b1=list(a)
        b1[0] = "dinesh"
        a=tuple(b1)
        print(a)
    # conversion_tuple()
    
    
class dict():
    #  used to store data in a key - value pair 
    # dictionary is orderd , changable ,and allow no duplicates
    def dict():
        d={
            1:"principal" ,
            2:"teachers" ,
            3:"students",
            "school_no":67 
        }
        print(d[1]) # this will return principal value of 1 here is principal
        # dict()
        # to determine how many items are ther in a list then we ill have to use len() method
        # here we can use any kind of data type "like the 4th element"
        
    def values():
        # inserting new values 4:"abc school"
         d={
            1:"principal" ,
            2:"teachers" ,
            3:"students",
            "school_no":67 
        }
         x=d.keys()
         print(x)
         d[4]="abc school"
         print(d)         
    # values()
    
        # to get keys use key() function
        # to get values use value() function
        # to get the items use items()
    
    def update():
        # dict also use update function to add more elements 
        d1={1: 'principal', 
            2: 'teachers', 
            3: 'students', 
            "school_no": 67, 
            4: 'abc school'
            }
        d1.update({"school_no":69})
        print(d1)
    # values()
    
    def pop():
        #we can use this method to eleminate the disered elements from the dict
         d1={1: 'principal', 
            2: 'teachers', 
            3: 'students', 
            "school_no": 67, 
            4: 'abc school'
            }
         d1.pop("school_no") #here we pop/delete the "key - value"  
         print(d1)
         
         #deletion is also done using del()
         
         del d1[3] # here we delete ke value 3-students 
         print(d1)
    #pop()  
        

    
    
    

    