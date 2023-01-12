n = int(input("N = "))
space = 2*n - 2
for i in range(1,2*n):
    stars = i
    if ( i > n) :
        stars = 2*n - i
    for j in range(1,stars+1):
        print("*",end="")
    for j in range(1,space+1):
        print(" ",end="")
    for j in range(1,stars+1):
        print("*",end="")
    print("")
    if(i<n):
        space -=2
    else:
        space +=2
    
# pattern
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *