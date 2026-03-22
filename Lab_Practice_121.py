#Check if a string is a palindrome.
n = input("Enter a string: ")
if n == n[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Check if a number is an Armstrong number.
n = int(input("Enter a number: "))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
    
#Display all numbers within a range except prime numbers.
n = int(input("Enter the range: "))
print("Numbers within the range except prime numbers:")
for i in range(1, n + 1):
    if i > 1:
        for j in range(2, int(i / 2) + 1):
            if (i % j) == 0:
                break
        else:
            continue
    print(i)

#Get the Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
    
#Find the factorial of a number.
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is", factorial)

#Remove duplicate/repetitive items from a list.
n = int(input("Enter the number of elements in the list: "))
my_list = []
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)
my_list = list(set(my_list))
print("List after removing duplicates:", my_list)

#Find the largest and smallest number in a list.
n = int(input("Enter the number of elements in the list: "))
my_list = []
for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)
print("Largest number:", max(my_list))
print("Smallest number:", min(my_list))

#Find all Anagrams in a list and group them together.
n = int(input("Enter the number of words in the list: "))
my_list = []
for i in range(n):
    word = input("Enter word: ")
    my_list.append(word)
anagram_dict = {}
for word in my_list:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]
print("Anagrams grouped together:")
for anagram_group in anagram_dict.values():
    print(anagram_group)
    
#Unpack a tuple into variables
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print("a:", a)
print("b:", b)
print("c:", c)

#Modify a list inside a nested tuple
my_tuple = (1, 2, [3, 4])
my_tuple[2][0] = 5
print("Modified tuple:", my_tuple)

#Use a lambda function to sort a list of tuples based on the second element.
my_list = [(1, 3), (2, 1), (3, 2)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print("Sorted list:", sorted_list)

#Convert two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print("Dictionary:", my_dict)

#Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)


#Find the common keys between two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
common_keys = set(dict1.keys()) & set(dict2.keys()) 
print("Common keys:", common_keys)

#Find the key with the maximum value in a dictionary
my_dict = {'a': 1, 'b': 5, 'c': 3}
max_key = max(my_dict, key=my_dict.get)     
print("Key with maximum value:", max_key)

#Nested dictionaries
nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
print("Nested dictionary:", nested_dict)


#Create a function that accepts a variable number of arguments.
def variable_arguments(*args):
    print("Arguments:", args)
variable_arguments(1, 2, 3)


# A function that calculates addition and subtraction and returns both results.
def add_subtract(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result = add_subtract(5, 3)
print("Addition:", result[0])
print("Subtraction:", result[1])

#A function that takes a list of numbers and returns the average.
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
print("Average:", average(numbers))

# Create A Calculator Class with methods for addition, subtraction, multiplication, and division.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(5, 3))
print("Multiplication:", calc.multiply(5, 3))
print("Division:", calc.divide(5, 3))

#Create A Calculator Class with methods for addition, subtraction, multiplication, and division using user input.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
calc = Calculator()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", calc.add(num1, num2))    
print("Subtraction:", calc.subtract(num1, num2))
print("Multiplication:", calc.multiply(num1, num2)) 
print("Division:", calc.divide(num1, num2))


#Create a class for a simple bank account with methods for deposit, withdrawal, and checking balance.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.check_balance()


#Print today's date in YYYY-MM-DD format
import datetime
today = datetime.date.today()
print("Today's date:", today.strftime("%Y-%m-%d"))
