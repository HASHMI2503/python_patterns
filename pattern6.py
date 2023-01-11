n = int(input("N = "))
for i in range(0,n+2):
    for j in range(1,n-i+1):
        print(j,end="")
    print("")
    
# pattern 
# 123456
# 12345
# 1234
# 123
# 12
# 1