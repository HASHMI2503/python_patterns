n = int(input("N = "))
for i in range(0,n+1):
    for j in range(0,n-i):
        print("*",end="")
    print("")

# pattern
# ******
# *****
# ****
# ***
# **
# *