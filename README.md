# AirBnB Clone Project

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects, forming the foundation for subsequent tasks in web development. This README file provides an overview of the project, its objectives, and requirements.

## Background Context

Before diving into the project, it's essential to familiarize yourself with the AirBnB concept. The primary goal of this project is to create a command interpreter that can manage AirBnB objects efficiently.

## Project Objectives

### 1. Base Classes and Serialization

- Implement a parent class (BaseModel) to handle the initialization, serialization, and deserialization of future instances.
- Develop a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File.
- Create classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
- Establish the first abstracted storage engine: File storage.
- Write unit tests to validate all classes and the storage engine.

### 2. Command Interpreter

- Build a command interpreter, similar to the Shell, but tailored to manage project objects.
- Enable the following functionalities:
  - Create a new object (e.g., User, Place).
  - Retrieve an object from a file, a database, etc.
  - Perform operations on objects (count, compute stats, etc.).
  - Update attributes of an object.
  - Destroy an object.

## Learning Objectives

By the end of this project, you should be able to:

- Create a Python package.
- Develop a command interpreter in Python using the cmd module.
- Implement unit testing in a large project.
- Serialize and deserialize a class.
- Read and write a JSON file.
- Manage datetime in Python.
- Understand and use UUIDs.
- Utilize *args and **kwargs in functions.
- Handle named arguments in a function.

## Copyright - Plagiarism

Respect the project guidelines regarding plagiarism. Do not copy and paste someone else's work. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Use allowed editors: vi, vim, emacs.
- Interpret/compile on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- End all files with a new line.
- The first line of all files should be #!/usr/bin/python3.
- Include a mandatory README.md file at the project's root.
- Code should adhere to pycodestyle (version 2.8.*).
- All files must be executable.
- The length of files will be tested using wc.
- Include documentation for modules, classes, and functions.

### Python Unit Tests

- All test files should end with a new line.
- Place test files inside a "tests" folder.
- Use the unittest module for tests.
- Test files should have a .py extension.
- All tests should be executed using `python3 -m unittest discover tests`.


## Execution

The shell should work in both interactive and non-interactive modes. For interactive mode:

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
