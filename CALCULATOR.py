print ("CALCULATOR MADE BY KASTAB")

a = float(input("Enter the first number")) # TAKE INPUT FROM THE USER AS INTEGER OR FLOAT
b = float(input("Enter the scond number")) #TAKE INPUT FROM THE USER AS INTEGER OR FLOAT

c = input("Enter the operator") #TAKE INPUT FROM THE USER

if c =='+': # PERFORM ADDITION
    print("THE SUM IS: ", a+b); # PRINTS THE ADDITION
    
elif c =='-': # PERFORMS SUBSTRACTION
    print("The difference is: ", a-b); #PRINTS THE RESULT AFTER SUBSTRACTION
    
elif c =='*': # PERFORMS MULTIPLICATION
    print("The product is: ", a*b) # PRINTS THE RESULT AFTER MULTIPLICATION

elif c =='/': #PERFORMS DIVISION
    print("ANSWER IS: ", a/b) # PRINTS THE ANSWER AFTER PERFORMING DIVISION
    
else: # IF THE USER PROVIDE ANY WRONG INPUT
    print("WRONG INPUT") # IT PRINTS THIS
