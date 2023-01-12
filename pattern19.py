n = int(input("N = "))

inis = 0
for i in range(1,n):
    for j in range(0,n-i):
        print("*",end="")
    for j in range(0,inis):
        print(" ",end="")
    for j in range(0,n-i):
        print("*",end="")
    inis += 2 
    print("")
inis = 6
for i in range(1,n):
    for j in range(0,i):
        print("*",end="")
    for j in range(0,inis):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    inis -= 2
    print("")
     
#  pattern
#  N = 5
# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********