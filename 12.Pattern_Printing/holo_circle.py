chr = "*"
r = int(input("Enter radius: "))
for i in range((r*2)+1):
    for j in range((r*2)+1):
        dist = ((i-r)**2 + (j-r)**2)**0.5
        if dist > r-0.5 and dist < r+0.5:
            print(chr,end="")
        else:
            print(" ",end="")
    print()
    
    
    
    
    