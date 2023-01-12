n = int(input("N = "))
for i in range(0,2*n - 1):
    for j in range(0,2*n - 1):
        top = i
        left = j
        right = (2*n - 2) - j
        down = (2*n - 2) - i
        print(n-min(min(top,down),min(left,right)),end=" ")
    print("")

# pattern
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5