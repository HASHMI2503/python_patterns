n = int(input("N = "))
arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(0,n+1):
    for j in range(0,i):
        print(arr[j],end="")
    print(end=" \n")

