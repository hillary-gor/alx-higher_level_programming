# Python - Input/Output

roject done during Full Stack Software Engineering studies at ALX AFRICA SE School.In this project, I practiced file handling in Python.  I used the builtin `with`, `open`, and `read` functions with the `json` module to read and write files and serialize and deserialize objects with JSON.

*****

## Tests :heavy_check_mark:

* [tests](./tests): This directory contains all my test files for this project:

### Table of contents

| File        | Prototype               |
| ------------| ----------------------- |
| [0-read_file.py](./0-read_file.py) | a function that reads a text file (UTF8) and prints it to stdout: | `def read_file(filename=""):` |
| [1-number_of_lines.py](./1-write_file.py) | a function that writes a string to a text file (UTF8) and returns the number of characters written: | `def number_of_lines(filename=""):` |
| [2-read_lines.py](./2-append_write.py) | a function that appends a string at the end of a text file (UTF8) and returns the number of characters added: | `def read_lines(filename="", nb_lines=0):` |
| [3-to_json_string.py](./3-to_json_string.py) | a function that returns the JSON representation of an object (string): | `def to_json_string(my_obj):` |
| [4-from_json_string.py](./4-from_json_string.py) | a function that returns an object (Python data structure) represented by a JSON string: | `def from_json_string(my_str):` |
| [5-save_to_json_file.py](./5-save_to_json_file.py) | a function that writes an Object to a text file, using a JSON representation: | `def save_to_json_file(my_obj, filename):` |
| [6-load_from_json_file.py](./6-load_from_json_file.py) | a function that creates an Object from a “JSON file”: | `def load_from_json_file(filename):` |
| [7-add_item.py](./7-add_item.py) | a script that adds all arguments to a Python list, and then save them to a file: | 
| [8-class_to_json.py](./8-class_to_json.py) | a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object: | `def class_to_json(obj):` | 
| [9-student.py](./9-student.py) | a class Student that defines a student by: |
| [10-student.py](./10-student.py) | a class Student that defines a student by: (based on 9-student.py) | 
| [11-student.py](11-student.py) | a class Student that defines a student by: (based on 10-student.py) | 
|[12-pascal_triangle.py](./12-pascal_triangle.py) | a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n: | `def pascal_triangle(n):` |
| [100-append_after.py](./100-append_after.py) | a function that inserts a line of text to a file, after each line containing a specific string (see example): | `def append_after(filename="", search_string="", new_string=""):` |
| [101-stats.py](101-stats.py) | a script that reads stdin line by line and computes metrics: | 

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text file to standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): Python function that writes a string to a UTF8 text file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON string representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): Python function that returns the Python object represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an object to a text file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an object from a `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments to a Python list saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans).

* **9. Student to JSON**
  * [9-student.py](./9-student.py): Python class `Student` that defines a student. Includes:
    * Public instance attributes `first_name`, `last_name`, and `age`.
    * Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
    * Public method `def to_json(self):` that returns the dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): Python class `Student` that defines a student. Builds on [11-student.py](./11-student.py) with:
    * Public method `def to_json(self, attrs=None):` that returns the dictionary representation of a `Student` instance.
    * If `attrs` is a list of strings, only the attributes listed are represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): Python class `Student` that defines a student. Builds on [12-student.py](./12-student.py) with:
    * Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance using the key/value pairs listed in `json`.
    * The method assumes `json` is a dictionary containing attributes with name/value corresponding to key/value.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): Python function that returns a list of lists of integers representing Pascal's triangle of size `n`.
  * Assumes the size parameter `n` is an integer.
  * If `n` is less than or equal to `0`, returns an empty list.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): Python function that inserts a line of text to a file after each line containing a specified string.

* **14. Log parsing**
  * [101-stats.py](./101-stats.py): Python script that reads lines from standard input. After every 10 lines or the input of a keyboard interruption (`CTRL + C`), computes the following metrics:
    * Total file size up that point: `File size: <total size>`
    * Status code of each read line, printed in ascending order:  `<status code>: <number>`
  * Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>`

*****


