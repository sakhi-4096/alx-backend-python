# Python - Variable Annotations
Variable annotations in Python allow you to provide additional information about variables, typically in the form of type hints, to help developers and tools understand the intended usage of those variables.

![Variable annotations](https://external-preview.redd.it/BBgDROEMSwzPp7gzMaNhep1si6zANHbYHhH8qvttn40.jpg?auto=webp&s=c43d0143bf40c942b948d7fd07ad9adfbddcd82d)

## Description
Variable annotations were introduced in Python 3.7 as part of PEP 526. Variable annotations are often used in conjunction with function annotations and class annotations to provide a more comprehensive type hinting system in Python, especially with the introduction of type-checkers like MyPy.

## Features
 * **Type Hints:** Variable annotations allow developers to provide type hints for variables. This helps in documenting the expected data type of a variable. While Python remains dynamically typed, type hints offer a form of static typing for better code understanding and tooling support.
 * **Optional and Informative:** Variable annotations are optional, and their absence does not affect the runtime behavior of the program. They serve as documentation and support for tools rather than imposing strict type requirements.
 * **Expressive Syntax:** Annotations are expressed using a colon (:) followed by the type hint. For example:
 ```python
 age: int = 19
 ```
 * **Compatibility with Existing Code:** Variable annotations can be added to existing codebases without requiring changes to the runtime behavior. Developers can gradually adopt type hints as needed.
 * **Used in Functions and Methods:** In addition to variables, annotations can be applied to function and method parameters, as well as return types, allowing for a more comprehensive type hinting system.
 * **Integration with Tooling:** Variable annotations are used by static analysis tools, linters, and IDEs to provide better code analysis, autocompletion, and early error detection.
 * **Type Checking Tools:** Type-checking tools like MyPy can be used to perform static analysis of the code and verify that the actual usage of variables aligns with the provided type hints.
 * **Annotations Beyond Types:** While type hints are the most common use case, variable annotations are not limited to types. They can be used for any expression, providing a more general-purpose annotation mechanism.
 
 ```python
 name: str = "Lindah"
 age: int = 9
 is_student: bool = True

 def great_person(person_name: str, person_age: int) -> str:
    return f"Hello, {person_name}! Your are {person_age} years old."
 ```

## Credits
 * [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
 * [Type hints cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Contact
 * [Twitter](https://www.twitter.com/sakhilelindah) / [Github](https://github.com/sakhi-4096) / [Mail](mailto:sakhilelindah@protonmail.com)