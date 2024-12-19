# Project: Python IO Toolkit

## Overview

This project aims to create a versatile Python toolkit for handling input/output operations, adhering to specific requirements and best practices. The toolkit includes various scripts that provide solutions for common file operations, configuration parsing, task management, data analysis, database interaction, document conversion, log file analysis, and unit testing.

## Requirements

### Python Scripts
- **Editors:** Allowed editors are vi, vim, and emacs.
- **Interpreter:** All scripts will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- **File Endings:** All files should end with a new line.
- **Shebang Line:** The first line of all scripts should be exactly `#!/usr/bin/python3`.
- **README.md:** A README.md file, at the root of the project folder, is mandatory.
- **Coding Style:** Code should follow the `pycodestyle` (version 2.8.*) guidelines.
- **Executable Files:** All scripts must be executable.
- **File Length:** The length of the files will be tested using `wc`.

### Python Test Cases
- **Editors:** Allowed editors are vi, vim, and emacs.
- **File Endings:** All files should end with a new line.
- **Test Folder:** All test files should be inside a folder named `tests`.
- **Test File Format:** All test files should be text files with the extension `.txt`.
- **Test Execution:** All tests should be executed using the command `python3 -m doctest ./tests/*`.
- **Documentation for Modules, Classes, and Functions:** Each module, class, and function should have proper documentation, accessible using commands like `python3 -c 'print(__import__("my_module").__doc__)'`, `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`, and `python3 -c 'print(__import__("my_module").my_function.__doc__)'`.

## Project Ideas and Descriptions

1. **File Operations Tool:**
   - **Description:** Create a Python script that performs various file operations such as copying, moving, renaming, and deleting files. Ensure that the script handles different file types and provides clear documentation for each function.

2. **Config File Parser:**
   - **Description:** Build a utility script that reads and parses configuration files in a custom format. It should be able to extract key-value pairs, handle comments, and provide a way to update and save changes to the configuration.

3. **Interactive Task List Manager:**
   - **Description:** Develop a command-line task manager that allows users to interactively add, delete, and mark tasks as completed. Store tasks in a file, and implement features such as priority levels, due dates, and categorization.

4. **CSV Data Analysis Tool:**
   - **Description:** Create a script that reads data from CSV files and performs basic analysis, such as calculating averages, sums, and generating summary reports. Ensure that the script is modular and can be easily extended for different data sets.

5. **Simple Database Interface:**
   - **Description:** Build a Python script that interacts with a simple database (e.g., SQLite). Implement basic CRUD operations (Create, Read, Update, Delete) and ensure that the script provides clear error handling and documentation.

6. **Markdown to HTML Converter:**
   - **Description:** Develop a script that converts Markdown files to HTML. Pay attention to formatting, headings, lists, and links. Include options for custom styling and ensure the generated HTML is well-formed.

7. **Log File Analyzer:**
   - **Description:** Create a tool that analyzes log files, extracts relevant information, and generates reports. Implement functionalities such as filtering by date, severity, or specific keywords. The tool should be able to handle logs in various formats.

8. **Unit Testing Framework:**
   - **Description:** Develop a simple unit testing framework that allows users to write and run tests for their Python scripts. Include features such as test discovery, fixtures, and assertions. The framework should generate clear and informative test reports.
