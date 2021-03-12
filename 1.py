'''  
Question-------
1 - Print the following patterns with a py script 
       
PATTERN 1-------       
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

PATTERN 2--------
A 
B C 
D E F 
G H I J 
K L M N O


'''
def print_star_pattern(n):
    for i in range(n):            # loop for each row of the pattern
        
        for k in range(5-i-1):    # to print spaces for every row
            print(" ",end=" ")
            
        for j in range(i+1):      # to print * for every row
            print("*",end=" ")
            
        print()                   # to go to next line
def print_alphabet_pattern(n):
    
    # ASCII values of A-Z are in range of 65-90 (both inclusive)
    
    t=65 # taking ASCII value of A
    
    for i in range(n):            # loop for each row of the pattern
    
        for j in range(i+1):      # to print ALPHABET for every row
            print(chr(t),end=" ")
            t+=1                  # increasing ascii value
            
        print()                   # to go to next line
    
        
n=5            # we can generalize this code by taking user input with n=int(input())
print_star_pattern(n)  # to print PATTERN 1
print_alphabet_pattern(n) # to print PATTERN 2
    

        
