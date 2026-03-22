# 90:-CREATE a list with random data types elements
# my_list = [42, "Hello", 3.14, True, None]
# print(my_list)


# 91:-print All elements of a list in a single line

# my_list = [42, "Hello", 3.14, True, None]
# print(*my_list)


# 92:-Count the number of elements in a list
# my_list = [42, "Hello", 3.14, True, None]
# print(len(my_list))

# 93:-Reverse the order of elements in a list

# my_list = [42, "Hello", 3.14, True, None]
# my_list.reverse()
# print(my_list)


# 94:-Square the elements of a list
# my_list = [42, "Hello", 3.14, True, None]
# my_list = [x**2 for x in my_list if isinstance(x, (int, float))]
# print(my_list)


# 95:-Remove An Element From A List
# my_list = [42, "Hello", 3.14, True, None]
# my_list.remove("Hello")
# print(my_list)


# 96:-Append An Element To A List
# my_list = [42, "Hello", 3.14, True, None]
# my_list.append("World")
# print(my_list)


# 97:-Sum Of All Elements In A List
# my_list = [42, "Hello", 3.14, True, None]
# my_list = [x for x in my_list if isinstance(x, (int, float))]
# print(sum(my_list))



# 98:-Get the maximum element from a list
# my_list = [42, "Hello", 3.14, True, None]
# my_list = [x for x in my_list if isinstance(x, (int, float))]
# print(max(my_list))


#99:-Remove Duplicates From A List
# my_list = [42, "Hello", 3.14, True, None, 42]
# my_list = list(set(my_list))
# print(my_list)



#100:-Choose Random Element From A List
# my_list = [42, "Hello", 3.14, True, None]
# import random
# print(random.choice(my_list))


#101:-Append Data Of The second List
# my_list = [42, "Hello", 3.14, True, None]
# second_list = [100, "World", 2.71, False, None]
# my_list.extend(second_list)
# print(my_list)


#102:-Filter odd and even numbers from a list
# my_list = [42, "Hello", 3.14, True, None]
# my_list = [x for x in my_list if isinstance(x, (int, float))]
# odd_numbers = [x for x in my_list if x % 2 != 0]
# even_numbers = [x for x in my_list if x % 2 == 0]
# print("Odd numbers:", odd_numbers)
# print("Even numbers:", even_numbers)


#103:-Enter or append n numbers in a list
# my_list = []
# n = int(input("Enter the number of elements you want to add: "))
# for _ in range(n):
#     element = input("Enter an element: ")
#     my_list.append(element)
# print(my_list)


#104:-Remove repetitive items from a list
# my_list = [42, "Hello", 3.14, True, None, 42]
# my_list = list(dict.fromkeys(my_list))
# print(my_list)


#105:-Assigning New Values to List Elements (with output)
# my_list = [42, "Hello", 3.14, True, None]
# my_list[0] = 100
# my_list[1] = "World"
# my_list[2] = 2.71
# my_list[3] = False
# my_list[4] = "New Element"
# print(my_list)


#106:-Adding New Elements to the List (Add-772 to list)
# my_list = [42, "Hello", 3.14, True, None]
# my_list.append(772)
# print(my_list)


#107:-Adding Multiple New Elements to the List
# my_list = [42, "Hello", 3.14, True, None]
# my_list.extend([100, "World", 2.71, False, None])
# print(my_list)


#108:-Deleting a Value from the List (Delete 730)
# my_list = [42, "Hello", 3.14, True, None]
# my_list.remove(730)
# print(my_list)


#109:-Copy Or Clone A list
# my_list = [42, "Hello", 3.14, True, None]
# my_list_copy = my_list.copy()
# print(my_list_copy)


#110:-Check Common Member Between Two Lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = set(list1) & set(list2)
# print("Common elements:", common_elements)


#111:-Select Random Item from List
# my_list = [42, "Hello", 3.14, True, None]
# import random
# print(random.choice(my_list))


