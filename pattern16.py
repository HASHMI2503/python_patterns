n = int(input("N = "))

for i in range(0,n+1):
    currentCharacter = 64 + i
    for j in range(1,i+1):
        print(chr(currentCharacter),end="")
        
    print(end=" \n")
    
# pattern
# A
# BB
# CCC
# DDDD
# EEEEE