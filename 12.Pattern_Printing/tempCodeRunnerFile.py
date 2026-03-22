i = int(input("Enter a number: "))
for _ in range(i):
    print("*" * 5)

n = int(input("Enter A Number: "))
for i in range(n):
    for j in range(1,n+1):
        print(j, end=" ")
    print()