![enter image description here](https://consultarse.org/wp-content/uploads/2021/08/Airbnb_Lockup_Over_Gradient.png)


# Console
Our command interpreter is designed for a single use case (managing the objects of our project), so it is capable of:

-   Create a new object (for example, a new user or a new place) - Retrieve an object from a file, a database, etc. - Perform operations on objects (count, calculate statistics, etc.) - Update attributes of an object - Destroy an object

The console.py is a command interpreter in which we can create different objects, the methods started with "do_" allow us to use them as commands (see usage examples). The methods contained in this interpreter that we create or modify are.


Command                        |Description and Use 
|--------|--|
`empty line () :`| an empty line + ENTER does not execute anything.
`precmd () :` |hook method executed just before the command line is interpreted. Modify to allow comands in the way arg.command() .
`do_all () :` |shows all instances that are located in the .json file based on the class name or not.
`do_show () :` |prints the string representation of an instance based on the class name and id.
`do_create () :`| creates a new instance of a specific class and saves it (in the JSON file).
`do_destroy () :`| deletes an instance based on the class name and id.
`do_update () :`| update an instance based on the class name and ID by adding or updating an attribute
`do_count () :`| retrieve the number of instances of a class
`do_quit () :`| exits the program.
`do_EOF () :` |exit the program by typing Ctrl + d.



## Execution

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non - interactive mode, pipe any command in an execution of the file ` console.py ` on the command line. Your shell should work like this in ` interactive mode: `


```
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

But also in ` non-interactive mode: ` (like Shell project in C)

```
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

All tests must also pass in non-interactive mode: ` $ echo" python3 -m unittest discover tests "| bash `


## Directory: models

This folder contains all the moodules of the class and the folder called engine, that conteins the file_storage.py module.

-   The BaseModel is the unique class with instace attributes, all the rest have only class attributes in way we provide easy class description, provide default value of any attribute and in the future, provide the same model behavior for file storage or database storage.

**UML diagrams**

![enter image description here](https://camo.githubusercontent.com/9a1f5c5ec847a8f598b81b4f212f9222d2f0f865b91ba0cd28091d91e7d26c4d/68747470733a2f2f696d6167697a65722e696d616765736861636b2e636f6d2f696d673932322f373332382f5465774b5a502e6a7067)


# Files
This project contains the following files: 
``` 
├── models 
│ ├── __ pycache __ 
│ │ ├── __ init __ . CPython-38.pyc 
│ │ ├── base_model.cpython-38.pyc
│ │ └── storage.cpython-38.pyc
│ ├── engine
│ │ ├── file_storage.py
│ │ └── __ init __ .py 
│ ├── __ init __ .py 
│ ├── amenity.py 
│ ├── base_model.py 
│ ├── city.py 
│ ├─ ─ place.py 
│ ├── review.py 
│ ├── state.py 
│ └── user.py 
└── tests
│ ├── __pycache__
│ │ └── __init __. Cpython-38.pyc 
│ ├── modelos_prueba 
│ │ ├── __pycache__
│ │ │ ├── __init __. Cpython-38.pyc
│ │ │ └── test_base_model.cpython-38.pyc 
│ │ ├── motor
│ │ ├── __init __ . Pyc 
│ │ │  └── test_file_storage.py
│ │ ├── __ init __ .py 
│ │ ├── test_amenity.py
│ │ ├── test_base_model.py 
│ │ ├── test_city.py
│ │ ├── test_place.py
│ │ ├── test_review.py
│ │ ├── test_state.py
│ │ └── test_user.py 
│ └── __ init __ .py 
├── AUTORES 
├── README.md 
└──   console.py 
 ``` 
 
># Versión 
 7 de November de 2021.
># Autores 
- Julio Cesar Arenas
- Stefania Russi
