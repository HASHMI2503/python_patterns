n = int(input("N = "))
start = 1
for i in range(0,n):
        if(i%2 == 0):
            start =1
        else:
            start = 0
        for j in range(0,i+1):
            print(start,end="")
            start = 1-start
        print("")
    
# pattern
# 1
# 01
# 101
# 0101
# 10101