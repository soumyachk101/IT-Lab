# Lab Exam Practice Solutions
# This file contains solutions to the key questions from the syllabus
# Each question is implemented with clear code and explanations

import datetime
from collections import defaultdict

# ==========================================
# 1. Core Logic & Loops (The Classics)
# ==========================================

# Q43: Check if a string is a palindrome
def is_palindrome(s):
    """
    A palindrome reads the same forwards and backwards.
    We can check by comparing the string with its reverse.
    """
    # Remove spaces and convert to lowercase for case-insensitive check
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

# Example usage:
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("hello"))  # False

# Q45: Check if a number is an Armstrong number
def is_armstrong_number(num):
    """
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    For example, 153 = 1^3 + 5^3 + 3^3
    """
    if num < 0:
        return False
    str_num = str(num)
    power = len(str_num)
    sum_digits = sum(int(digit) ** power for digit in str_num)
    return sum_digits == num

# Example usage:
# print(is_armstrong_number(153))  # True
# print(is_armstrong_number(123))  # False

# Q47: Display all numbers within a range except prime numbers
def display_non_primes(start, end):
    """
    Display all numbers in the range [start, end] that are not prime.
    A prime number is greater than 1 with no positive divisors other than 1 and itself.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    non_primes = [num for num in range(start, end + 1) if not is_prime(num)]
    print(f"Non-prime numbers between {start} and {end}: {non_primes}")

# Example usage:
# display_non_primes(1, 20)

# Q48 / Q58: Get the Fibonacci series
def fibonacci_series(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Example usage:
# print(fibonacci_series(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Q49 / Q57: Find the factorial of a number
def factorial(n):
    """
    Factorial of n (n!) is the product of all positive integers less than or equal to n.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
# print(factorial(5))  # 120

# ==========================================
# 2. Lists & Sets (Data Manipulation)
# ==========================================

# Q99 / Q104 / Q89: Remove duplicate/repetitive items from a list
def remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving order.
    Convert to set and back to list.
    """
    return list(set(lst))

# Alternative preserving order:
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
# print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]

# Q113: Difference between `append` and `extend`
# append() adds a single element to the end of the list
# extend() adds all elements from an iterable to the end of the list

# Example:
# lst = [1, 2, 3]
# lst.append([4, 5])  # lst becomes [1, 2, 3, [4, 5]]
# lst = [1, 2, 3]
# lst.extend([4, 5])  # lst becomes [1, 2, 3, 4, 5]

# Q66, Q67, Q68: Create Intersection, Union, and Difference of Sets
def set_operations(set1, set2):
    """
    Perform basic set operations
    """
    intersection = set1 & set2  # or set1.intersection(set2)
    union = set1 | set2  # or set1.union(set2)
    difference = set1 - set2  # or set1.difference(set2)
    return intersection, union, difference

# Example usage:
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# inter, uni, diff = set_operations(s1, s2)
# print(f"Intersection: {inter}")  # {3, 4}
# print(f"Union: {uni}")  # {1, 2, 3, 4, 5, 6}
# print(f"Difference (s1 - s2): {diff}")  # {1, 2}

# Q86: Find all Anagrams in a list and group them
def group_anagrams(words):
    """
    Group words that are anagrams of each other.
    Anagrams are words with the same letters in different order.
    """
    anagram_groups = defaultdict(list)
    for word in words:
        # Sort the letters to create a key
        key = ''.join(sorted(word.lower()))
        anagram_groups[key].append(word)
    # Return groups with more than one word
    return [group for group in anagram_groups.values() if len(group) > 1]

# Example usage:
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(words))  # [['eat', 'tea', 'ate'], ['tan', 'nat']]

# ==========================================
# 3. Tuples & Dictionaries (Immutability & Key-Value Pairs)
# ==========================================

# Q117: Unpack a tuple into variables
def unpack_tuple():
    """
    Unpack a tuple into multiple variables
    """
    my_tuple = (1, 2, 3, 4, 5)
    a, b, c, d, e = my_tuple
    print(f"Unpacked: a={a}, b={b}, c={c}, d={d}, e={e}")

    # Unpack with * for remaining elements
    first, *middle, last = my_tuple
    print(f"First: {first}, Middle: {middle}, Last: {last}")

# Example usage:
# unpack_tuple()

# Q148: Modify a list inside a nested tuple
def modify_list_in_tuple():
    """
    Tuples are immutable, but if they contain mutable objects like lists,
    those mutable objects can be modified.
    """
    nested_tuple = (1, 2, [3, 4, 5], 6)
    print(f"Original: {nested_tuple}")
    # We can modify the list inside the tuple
    nested_tuple[2].append(6)
    print(f"After modifying list: {nested_tuple}")

# Example usage:
# modify_list_in_tuple()

# Q169: Convert two lists into a dictionary
def lists_to_dict(keys, values):
    """
    Convert two lists into a dictionary using zip()
    """
    return dict(zip(keys, values))

# Example usage:
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# print(lists_to_dict(keys, values))  # {'a': 1, 'b': 2, 'c': 3}

# Q170: Merge two dictionaries
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries. If there are duplicate keys, values from dict2 will override dict1.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

    # Alternative using dictionary unpacking (Python 3.5+)
    # return {**dict1, **dict2}

# Example usage:
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# print(merge_dicts(d1, d2))  # {'a': 1, 'b': 3, 'c': 4}

# Q171 / Q172: Nested dictionaries
def nested_dict_operations():
    """
    Working with nested dictionaries
    """
    nested_dict = {
        'person': {
            'name': 'John',
            'age': 30,
            'address': {
                'street': '123 Main St',
                'city': 'Anytown'
            }
        }
    }

    # Access nested values
    name = nested_dict['person']['name']
    city = nested_dict['person']['address']['city']
    print(f"Name: {name}, City: {city}")

    # Modify nested values
    nested_dict['person']['age'] = 31
    nested_dict['person']['address']['city'] = 'New Town'
    print(f"Updated dict: {nested_dict}")

# Example usage:
# nested_dict_operations()

# ==========================================
# 4. Functions & Modules (Reusability)
# ==========================================

# Q213: Create a function that accepts a variable number of arguments
def variable_args_function(*args):
    """
    Function that accepts a variable number of arguments using *args
    """
    print(f"Number of arguments: {len(args)}")
    print(f"Arguments: {args}")
    total = sum(args)
    print(f"Sum: {total}")
    return total

# Example usage:
# variable_args_function(1, 2, 3, 4, 5)

# Q214: A function that calculates addition and subtraction and returns both
def add_and_subtract(a, b):
    """
    Function that calculates both addition and subtraction and returns both results
    """
    addition = a + b
    subtraction = a - b
    return addition, subtraction  # Returns a tuple

# Example usage:
# add_result, sub_result = add_and_subtract(10, 5)
# print(f"Addition: {add_result}, Subtraction: {sub_result}")  # Addition: 15, Subtraction: 5

# Q186: Print today's date in YYYY-MM-DD format
def print_today_date():
    """
    Print today's date using the datetime module
    """
    today = datetime.date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    print(f"Today's date: {formatted_date}")
    return formatted_date

# Example usage:
# print_today_date()

# ==========================================
# Main execution (uncomment to test)
# ==========================================

if __name__ == "__main__":
    print("=== Testing Core Logic & Loops ===")
    print(f"Palindrome 'radar': {is_palindrome('radar')}")
    print(f"Armstrong 153: {is_armstrong_number(153)}")
    display_non_primes(1, 20)
    print(f"Fibonacci first 10: {fibonacci_series(10)}")
    print(f"Factorial 5: {factorial(5)}")

    print("\n=== Testing Lists & Sets ===")
    print(f"Remove duplicates [1,2,2,3]: {remove_duplicates([1,2,2,3])}")
    s1, s2 = {1,2,3}, {2,3,4}
    inter, uni, diff = set_operations(s1, s2)
    print(f"Sets intersection: {inter}, union: {uni}, difference: {diff}")
    words = ["eat", "tea", "tan", "ate"]
    print(f"Anagram groups: {group_anagrams(words)}")

    print("\n=== Testing Tuples & Dictionaries ===")
    unpack_tuple()
    modify_list_in_tuple()
    print(f"Lists to dict: {lists_to_dict(['x','y'], [10,20])}")
    d1, d2 = {'a':1}, {'b':2}
    print(f"Merged dicts: {merge_dicts(d1, d2)}")
    nested_dict_operations()

    print("\n=== Testing Functions & Modules ===")
    variable_args_function(1,2,3)
    add, sub = add_and_subtract(8, 3)
    print(f"Add: {add}, Sub: {sub}")
    print_today_date()
