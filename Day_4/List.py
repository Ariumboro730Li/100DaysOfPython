"""

1 / 2

When I mention that Python lists offer more flexibility and a richer set of operations and methods compared to arrays in PHP, I'm referring to the following aspects:

!! Dynamic Size: In Python !!, 
lists are dynamically sized, 
meaning they can grow or shrink as needed. 
You can add or remove elements 
from a list without explicitly specifying its size.
PHP arrays, on the other hand, 
have a fixed size and require manual resizing or manipulation.

!! Heterogeneous Data Types !!: 
Python lists can store elements of different data types 
within the same list. 
For example, a list can contain integers, strings, floats, 
and other objects. PHP arrays can also store elements 
of different types, but they are not as flexible 
in terms of type handling compared to Python lists.

!! Built-in Methods: !!
Python provides a comprehensive set of 
built-in methods for manipulating lists. 
These methods include appending elements, 
removing elements, sorting, reversing, slicing, 
searching, and more. 
Python's list methods allow for convenient and efficient 
list manipulation. While PHP arrays have some similar functionality, 
Python lists offer a more extensive range of built-in methods.

!! List Comprehension: !!
Python supports list comprehensions, 
which are concise and powerful ways to create 
lists based on existing lists or other iterable objects. 
List comprehensions provide a compact syntax 
for generating new lists based on certain criteria or transformations. 
PHP arrays do not have a direct equivalent to list comprehensions.

!! Flexibility in Indexing: !!
Python lists support both positive 
and negative indexing. 
Positive indexing starts from 0 and allows you to access elements
from the beginning of the list. 
Negative indexing starts from -1 and allows you to access
elements from the end of the list. 
This provides flexibility and convenience when working with lists.
PHP arrays primarily use positive indexing.

Overall, Python lists provide a more versatile and 
feature-rich data structure compared to arrays in PHP. 
They offer greater flexibility in terms of size management, 
support for different data types, a comprehensive set 
of built-in methods, 
list comprehensions, and more flexible indexing options.
"""

my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [1, 10, 4, 5, 6]

# Slicing
sliced_list = my_list[1:4]
print(sliced_list)  # Output: [10, 4, 5]
