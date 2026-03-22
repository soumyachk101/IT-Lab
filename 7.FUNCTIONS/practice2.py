#Square Function

def square(number):
    return number ** 2

result = square(5)
print(result)


#Create a function that takes different parameters
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info("Soumya", 20)




#Write a function that multiplies two numbers but can also accept and multiply strings
def multiply(a, b):
    return a * b

print(multiply(3, 4))        # Outputs: 12
print(multiply("Hi ", 3))    # Outputs: Hi Hi Hi



#Create a function that returns both the area and circumference of a circle given its radius
import math

def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
area, circumference = circle_properties(3)
print(f"Area: {area}, Circumference: {circumference}")


#Write a function that greets a user.If no name is provided, it should greet with a default name
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("Soumya")  # Outputs: Hello, Soumya!
greet()         # Outputs: Hello, Guest!    