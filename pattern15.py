n = int(input("N = "))
num = n
for i in range(n):
    currentCharacter = 65
    for j in range(1, num+1):
        print(chr(currentCharacter), end=" ")
        currentCharacter += 1
    print()
    num -= 1
    
# pattern
# A B C D E
# A B C D
# A B C
# A B
# A