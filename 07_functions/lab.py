#Write a function to print "Hello, World!"
def hello_world():
    return "Hello, World!"
print(hello_world())

#Write a function that takes a name as argument and prints “Hello, [name]!”
def hello_name(name):
    return f"Hello, {name}!"
print(hello_name("Soumya"))

#Write a function that returns the square of a number
def square(num):
    return num*num
print(square(5))


#Write a function to check whether a number is even or odd.
def is_even(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"
print(is_even(10))


#Write a function to find the maximum of two numbers.
def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_of_two(5,7))

#Write a function to calculate the factorial of a number.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))



#Write a function to calculate the area of a circle given its radius.
import math
def area_of_circle(radius):
    return math.pi * radius * radius
print(area_of_circle(7))



#Write a function that takes a list and returns the sum of all elements.
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_of_list([1,2,3,4,5]))



#Write a function that converts Celsius to Fahrenheit.
import math
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))




#Write a function to find the length of a given string.
def length_of_string(s):
    return len(s)
print(length_of_string("Hello, World!"))



#Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
def func1(*args):
    for arg in args:
        print(arg)
func1(1, 2, 3, "Hello", True)




#Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement
def calculation(a, b):
    return a + b, a - b
print(calculation(10, 5))
