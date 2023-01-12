n =int(input("N = "))
for i in range(0,n):
    
    for j in range(0,n-i-1):
        print(" ",end="")
        
    alphabet = 65
    breakpoint = (2*i+1)/2 
     
    for j in range(0,2*i + 1):
        print(chr(alphabet),end="")
        if j<=breakpoint:
            alphabet +=1
        else:
            alphabet -= 1
            
            
    for j in range(0,n-i-1):
        print(" ",end="")
    print("\n")

# pattern
#     A

#    ABC

#   ABCDC

#  ABCDEDC

# ABCDEFEDC