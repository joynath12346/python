""""
Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program.
Sample:
> Enter input: 2
> 2 is positive
> -3
> -3 is negative
> “Quit”
> (stop the program)
""""


while (True):
    
    x = input("Enter input: ")
    
    if (x == "Quit"):
        break
    
    else:
        
        x = int(x)
        
        print (f"{x} is" , end=" ")
    
        if x > 0:
            print ("positive")
            
        elif x < 0:
            print ("negative")
            
        else:
            print ("zero")
