# if u want to run a specific function then please remove the # sypbol on the function call on last part of the respective functions/def  

class loops:
    # loops are mainly used for itration purpose 
    # as a programmer we have to itrate through thousands of data to make this easy loops where invented 
    # diffrent kinds of loops include 
                        # for loop
                        # while loop 
                        # for else loop
    def for_loop():
        # for loop is used for itrating over a sequence which include list,tuple,dict,string etc...
        list=["apple","bannana","garpe","mango"]
        for i in list:
            print(i)
            # we get the list of fruits in the list  
    
        # looping through a string 
        for i in "bannana":
            print("\n",i)
            
    
        
        # BREAK 
        # break is a statement used to exit from a loop 
        
        # CONTINUE
        # continue is a statement used to skip a part in the loop when a certain condition is met
        
        # RANGE
        # range() is used to specifie the range of numbers that the for loop has to cover
        
        for i in range(1,100):
            print(i) # will print nos from 1 to 100   
           
        for i in range(1,100,5):
            print(i) #this will print from 1 to 100 with the intervel of 5

    #for_loop()

    def for_else():
        # here we have a loop which does a specific task assigned by the user when the loop is finished 
        
        for i in range(9):
            print(i)
        else:
            print("LOOP HAS COMPLETED SUCCESFULLY")
            
        # here after itrating through 9th element it will print "loop has completed succesfully"
        
        # else will not be executed with a break statement if used
        
        # there is also nested loop [loop within a loop]
        
        # pass statement loops cannot be empty so sometimes pass statements are used to avoid error
        
        for i in range(1,7,2):
            pass
        
        #here ther is no output and no error 
        
    # for_else()
    
    
    def while_loop():
        # while loop is used to execute the code untill a certain conditiion is met
        # or 
        # in other words it exicutes infinitly if no condition is met
        
        i=1
        while i<6:
            print(i)
            i+=1
            
        # basic structure of while loop
        # print from 1 to 5 
        
        # break statements is used to exit from the loop even if the while condition is true
        
        i=1
        while i<6:
            print(i)
            if i==4:
                break
            i+=1
         
        #  also we have the else statement
        # here after the loop is fullfilled else condition is triggerd
        
        i=1
        while i<6:
            print(i)
            i+=1
        else:
            print("loop ended")        
            
    # while_loop()
            