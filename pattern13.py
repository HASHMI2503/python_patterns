n = int(input("N = "))
num = 1
for i in range(0,n+1):
    for j in range(0,i):
       print(num,end=" ")
       num +=1
    print("")        
    
# pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15