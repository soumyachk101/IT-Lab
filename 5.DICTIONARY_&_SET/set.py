# set = {"soumya", "soumya1", "soumya2", "soumya3"}
# print(set) # Output: {'soumya', 'soumya1', 'soumya2', 'soumya3'}


#Add Member(s) to a Set :-

# set = {"Soumya","Mohit","Soham","Suvo"}
# set.add("S")
# print(set)  # Output: {'Soumya', 'Mohit', 'Soham', 'Suvo', 'S'}


#Remove Item(s) from a Given Set :-
# set = {1,2,3,4,5,6,7,8,9,10}
# set.remove(6)
# print(set)  # Output: {1, 2, 3, 4, 5, 7, 8, 9, 10}

# Remove an Item from a Set if Present :-

# set = {1,2,3,4,5,6,7,8,9,10}
# set.discard(6)
# print(set)  # Output: {1, 2, 3, 4, 5, 7, 8, 9, 10}


#Create an Intersection of Sets:-

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# set3 = set1.intersection(set2)
# print(set3)  # Output: {4, 5}


# Create a Union of Sets:-
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# set3 = set1.union(set2)
# print(set3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}


# Create a Difference of Sets:-
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# set3 = set1.difference(set2)
# print(set3)  # Output: {1, 2, 3}


# Create a Symmetric Difference of Sets:-
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# set3 = set1.symmetric_difference(set2)
# print(set3)  # Output: {1, 2, 3, 6, 7, 8}

# Create a Subset of a Set:-
# set1 = {1,2,3,4,5}
# set2 = {2,3,4}
# is_subset = set2.issubset(set1)   
# print(is_subset)  # Output: True


# Create a Superset of a Set:-
# set1 = {1,2,3,4,5}
# set2 = {2,3,4}
# is_superset = set1.issuperset(set2)
# print(is_superset)  # Output: True


# Create a Frozen Set:-
# frozen_set = frozenset([1, 2, 3, 4, 5])
# print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})


# Create a Set from a List:-
# list_data = [1, 2, 3, 4, 5]
# set_from_list = set(list_data)
# print(set_from_list)  # Output: {1, 2, 3, 4, 5}


# Create a Set from a Tuple:-
# tuple_data = (1, 2, 3, 4, 5)
# set_from_tuple = set(tuple_data)
# print(set_from_tuple)  # Output: {1, 2, 3, 4, 5}


# Create a Set from a String:-
# string_data = "hello"
# set_from_string = set(string_data)
# print(set_from_string)  # Output: {'h', 'e', 'l', 'o'}


# Create a Set from a Dictionary:-
# dict_data = {"name": "Soumya", "age": 19}
# set_from_dict = set(dict_data)
# print(set_from_dict)  # Output: {'name', 'age'}


