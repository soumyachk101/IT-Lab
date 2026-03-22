def sum(a,b):
    c = a+b
    return c
print(sum(3,4))



#avarage of 3 numbers

def avarage(x,y,z):
    if(x==0 and y==0 and z==0):
        return 0
    sum = x+y+z
    return sum/3
print(avarage(0,4,8))




#factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

