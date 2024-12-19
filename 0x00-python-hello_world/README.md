# Python - hello_world

project done during Full Stack Software Engineering studies at __ALX AFRICA SE School__. aims at learning how to use the interpreter, printing text and variables, indexing and slicing strings in `Python`

## test 📁
- [test](./tests/): This directory contains all my test files for this project.

## Lists.h
* [lists.h](./lists.h): Header file containing prototypes for all functions written in the project.

_Filename_ | _Description_ | _Prototype_
-----------|---------------|------------
[0-run](./0-run) | a Shell script that runs a Python script. |
[1-run_inline](./1-run_inline) | a Shell script that runs Python code. |
[2-print.py](./2-print.py) | a Python script that prints exactly "Programming is like building a m…|
[3-print_number.py](./3-print_number.py) | a script that print the integer stored in the variable number, followed by Battery street, followed by a new line. |
[4-print_float.py](./4-print_float.py) | print the float stored in the variable number with a precision of 2 digits. |
[5-print_string.py](5-print_string.py) | print 3 times a string stored in the variable str, followed by its first 9 characters. |
[6-concat.py](6-concat.py) | print Welcome to Holberton School! |
[7-edges.py](7-edges.py) | print the first 3, last 2 and middle words of Holberton |
[8-concat_edges.py](8-concat_edges.py) | print object-oriented programming with Python, followed by a new line. |
[9-easter_egg.py](9-easter_egg.py) | a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line. |
[10-check_cycle.c](10-check_cycle.c) | a function in C that checks if a singly linked list has a cycle in it. | `int check_cycle(listint_t *list)`
[100-write.py](100-write.py) | a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line. |
[101-compile](101-compile) | a script that compiles a Python script file. |
[102-magic_calculation.py](102-magic_calculation.py) | python magic file |


## Tasks 🛅

0. **Run Python File**
    - [0-run](./0-run): Bash script that runs a Python script file saved in the environment variable `$PYFILE`.


1. **Run inline**
    - [1-run_inline](./1-run_inline): Bash script that runs Python code saved in the environment variable `$PYCODE`.


2. **Hello, print**
    - [2-print.py](./2-print.py): Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line using the function `print`.


3. **Print integer**
    - [3-print_number.py](./3-print_number.py): Python script that prints the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py).


4. **Print float**
    - [4-print_float.py](./4-print_float.py): Python script that prints the float stored in the variable `number` with a precision of two digits.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py).


5. **Print string**
    - [5-print_string.py](5-print_string.py): Python script that prints a string stored in the variable `str` three times, then a new line, then the first nine characters contained in `str`, followed by another new line.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py).


6. **Play with strings**
    - [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py).


7. **Copy - Cut - Paste**
    - [7-edges.py](7-edges.py): Python script that sets three string variables based on the string contained in the variable `word` as follows:
    - `word_first_3`: Contains the first three letters of the variable `word`.
    - `word_last_2`: Contains the last two letters of the variable `word`.
    - `middle_word`: Contains the value of the variable `word` without the first and last letters.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).


8. **Create a new sentence**
    - [8-concat_edges.py](8-concat_edges.py): Python script that prints `object-oriented programming with Python`, followed by a new line without creating new variables or string literals.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).


9. **Easter Egg**
    - [9-easter_egg.py](9-easter_egg.py): Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.


10. **Linked list cycle**
    - [10-check_cycle.c](10-check_cycle.c): C function that checks if a linked list contains a cycle.
    - Returns `0` if there is no cycle and `1` if there is.
    - Helper files:
      * [linked_lists.c](./tests/10-linked_lists.c): C functions handling linked lists for testing [10-check_cycle.c](./10-check_cycle.c) (provided by Holberton School).
      * [lists.h](./lists.h): Header file containing definitions and prototypes for all types and functions used in [linked_lists.c](./tests/10-linked_lists.c) and [10-check_cycle.c](./10-check_cycle.c).


11. **Hello, write**
    - [100-write.py](./100-write.py): Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using the function `write` from the `sys` module.
    - Exits with a status code of `1`.


12. **Compile**
    - [101-compile](./101-compile): Python script that compiles a Python script file stored in the environment variable `$PYFILE` and saves it to an output file `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).


13. **ByteCode -> Python #1**
    - [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a bytecode provided by Holberton School.
