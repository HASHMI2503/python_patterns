n = int(input("N = "))
num = 1
space = (n - 1) * 2
for i in range(n):
    currentNumber = 1
    for j in range(1, num+1):
        print(currentNumber, end=" ")
        currentNumber += 1
    for j in range(1, space+1):
        print(" ", end=" ")
    currentNumber -= 1
    for j in range(1, num+1):
        print(currentNumber, end=" ")
        currentNumber -= 1
    
    print()

    num += 1
    space -= 2

# pattern
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1