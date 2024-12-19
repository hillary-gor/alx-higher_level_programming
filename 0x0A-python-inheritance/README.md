# 0x0A. Python - Inheritance

## Project Title

This project focuses on understanding and implementing concepts related to inheritance in Python.

## Requirements

- Python Scripts
  - Allowed editors: vi, vim, emacs
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Code should use pycodestyle (version 2.8.*)
  - All files must be executable
  - Length of files will be tested using `wc`

- Python Test Cases
  - Allowed editors: vi, vim, emacs
  - All files should end with a new line
  - All test files should be inside a folder `tests`
  - All test files should be text files (extension: .txt)
  - All tests should be executed by using this command: `python3 -m doctest ./tests/*`
  - All modules, classes, and functions should have documentation

- Documentation
  - Do not use the words `import` or `from` inside your comments
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method

## Tasks :heavy_check_mark:

### 0. Lookup

Implement a function `def lookup(obj):` that returns the list of available attributes and methods of an object.

### 1. MyList

Implement a class `MyList` that inherits from `list`.

### 2. Is Same Class

Implement a function `def is_same_class(obj, a_class):` that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

### 3. Is Kind of Class

Implement a function `def is_kind_of_class(obj, a_class):` that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

### 4. Inherits From

Implement a function `def inherits_from(obj, a_class):` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

### 5. Geometry module

Create an empty class `BaseGeometry`.

### 6. Improve Geometry

Create a class `BaseGeometry` (based on 5-base_geometry.py) with additional functionality.

### 7. Integer validator

Create a class `BaseGeometry` (based on 6-base_geometry.py) with integer validation.

### 8. Rectangle

Create a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py).

### 9. Full Rectangle

Create a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py) and adds width and height validation.

### 10. Square #1

Create a class `Square` that inherits from `Rectangle` (9-rectangle.py).

### 11. Square #2

Create a class `Square` that inherits from `Rectangle` (9-rectangle.py) with additional functionality.

### 12. My Integer

Create a class `MyInt` that inherits from `int`.

### 13. Can I?

Implement a function `def add_attribute(obj, attribute, value):` that adds a new attribute to an object if it’s possible.


