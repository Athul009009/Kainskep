# Match case in python its syntax look more like if-else statement
# it is similer to switch case in c - java 

# example is as shown
from unittest import case
from soupsieve import match


c = "python is life"
match c:
    case "python is life":
        print("Bro welcome to wonderful world of python")
    case "python is not good":
        print("Its not true")
    case other:
        print("!!!")

# its mainly used nowa days because of its simplicity 
        