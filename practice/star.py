num = int(input("Enter a number"))
x = num

for i in range(0, num):
    for l in range(0, x):
        print(" ", end="")
    x = x - 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print()
