n = int(input("N = "))
for i in range(0,n):
    alphabet = 65 + n - 1
    for j in range(0,i+1):
        print(chr(alphabet),end="")
        alphabet -=1
    print(end=" \n")

# pattern
# J
# JI
# JIH
# JIHG
# JIHGF
# JIHGFE
# JIHGFED
# JIHGFEDC
# JIHGFEDCB
# JIHGFEDCBA