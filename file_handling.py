class files:
    # Files are mainly used as a orderd storage fecility or it is simply a storage 
    
    # there are 3 main operations used in python they are as follows 

                        # read
                        # write 
                        # append

    # default is read 
    
    def file_write():
        
        file1 = open("1.txt","w") # here a file named file1 is created on write mode
        file1.write("hello") # printed hello inside the 1.txt file
    # file_write()
    
    
    def file_read():
        
        #  here we read the file (its contents) that we created
         
        file1 = open("1.txt","r")
        print(file1.read())
        
    # file_read()
    
    def file_append():
        
        # here we add content to the already existing file through append method
        
        file1 = open("1.txt","a")
        file1.write("\n HOW R U")
        print(file1.read())
        file1.close()
    file_append()
        
        
    
        