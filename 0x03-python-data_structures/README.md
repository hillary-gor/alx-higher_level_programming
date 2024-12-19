# Python - Data Structures: Lists, Tuples

project done during Full Stack Software Engineering studies at **ALX AFRICA SE School**. In this project, I learned about Data sturctures, Lists, Tuples in python

## test 📁

- [tests](./tests/): This directory contains all my test files for this project.

## Lists.h

[lists.h](./lists.h): Header file for the C program

| _Filename_                                                             | _Description_                                                                                                             | _Prototype_                                    |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [0-print_list_integer.py](./0-print_list_integer.py)                   | Python function that prints all integers of a list                                                                        | `def print_list_integer(my_list=[]):`          |
| [1-element_at.py](./1-element_at.py)                                   | Python function that retrieves an element from a list like in C                                                           | `def element_at(my_list, idx):`                |
| [2-replace_in_list.py](./2-replace_in_list.py)                         | Python function that replaces an element of a list at a specific position (like in C)                                     | `def replace_in_list(my_list, idx, element):`  |
| [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py) | Python function that prints all integers of a list, in reverse order                                                      | `def print_reversed_list_integer(my_list=[]):` |
| [4-new_in_list.py](./4-new_in_list.py)                                 | Python function that replaces an element in a list at a specific position without modifying the original list (like in C) | `def new_in_list(my_list, idx, element):`      |
| [5-no_c.py](./5-no_c.py)                                               | Python function that removes all characters c and C from a string                                                         | `def no_c(my_string):`                         |
| [6-print_matrix_integer.py](./6-print_matrix_integer.py)               | Python function that prints a matrix of integers                                                                          | `def print_matrix_integer(matrix=[[]]):`       |
| [7-add_tuple.py](./7-add_tuple.py)                                     | Python function that adds 2 tuples                                                                                        | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| [8-multiple_returns.py](./8-multiple_returns.py)                       | Python function thatreturns a tuple with the length of a string and its first character                                   | `def multiple_returns(sentence):`              |
| [9-max_integer.py](./9-max_integer.py)                                 | Python function that finds the biggest integer of a list                                                                  | `def max_integer(my_list=[]):`                 |
| [10-divisible_by_2.py](./10-divisible_by_2.py)                         | Python function that finds all multiples of 2 in a list                                                                   | `def divisible_by_2(my_list=[]):`              |
| [11-delete_at.py](./11-delete_at.py)                                   | Python function that deletes the item at a specific position in a list                                                    | `def delete_at(my_list=[], idx=0):`            |
| [12-switch.py](./12-switch.py)                                         | Python program that completes source code in order to switch value of a and b                                             |
| [13-is_palindrome.c](./13-is_palindrome.c)                             | C program that checks if a singly linked list is a palindrome                                                             |

## Tasks 🛅


0. **Print a list of integers**

  - [0-print_list_integer.py](./0-print_list_integer.py): Python program that prints all integers of a list.
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

1. **Secure access to an element in a list**

   - [1-element_at.py](./1-element_at.py): Python program that retrieves an element from a list like in C.
     - If `idx` is negative, the function should return None
     - If `idx` is out of range (> of number of element in my_list), the function should return `None`
     - You are not allowed to import any module
     - You are not allowed to use `try/except`

2. **Replace element**

   - [2-replace_in_list.py](./2-replace_in_list.py): Python program that replaces an element of a list at a specific position (like in C).
     - If `idx` is negative, the function should not modify anything, and returns the original list
     - If `idx` is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
     - You are not allowed to import any module
     - You are not allowed to use `try/except`

3. **Print a list of integers... in reverse!**

   - [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py): Python program that prints all integers of a list, in reverse order.
     - Format: one integer per line. See example
     - You are not allowed to import any module
     - You can assume that the list only contains integers
     - You are not allowed to cast integers into strings
     - You have to use `str.format()` to print integers

4. **Replace in a copy**

   - [4-new_in_list.py](4-new_in_list.py): Python program that replaces an element in a list at a specific position without modifying the original list (like in C)
     - If `idx` is negative, the function should return a copy of the original list
     - If `idx` is out of range (> of number of element in my_list), the function should return a copy of the original `list`
     - You are not allowed to import any module
     - You are not allowed to use `try/except`

5. **Can you C me now?**
   - [5-no_c.py](5-no_c.py): Python program that removes all characters c and C from a string.
     - The function should return the new string
     - You are not allowed to import any module
     - You are not allowed to use `str.replace()`
