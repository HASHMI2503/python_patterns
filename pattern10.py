n = int(input("N = "))
for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    print("")
for i in range(0,n):
    for j in range(0,n-i):
            print("*",end="")
    print("")
        
# pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *