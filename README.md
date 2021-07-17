# Basic Calculator
> A calculator package that performs simple add/subtract, divide/mulitply functions and takes the nth root of a number


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Installation] (#installation)
* [Functions](#functions)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
<!-- * [License](#license) -->


## General Information
- This project is a simple calcuator package to perform basic add/subtract, divide/mulitply functions and to take the nth root of a number. 
- This project is to apply my knowledge in creating a python package from start to finish, as well as write clean OOP based Python code and testing it



## Technologies Used
- Python - version 3.6

## Installation 
### Install from GitHub
To install, run the following command in a terminal/commnd prompt.
```bash
pip install git+https://github.com/GraceFad/Calculator.git
```

To import calculator package for use and test the functions, run the following command.

```python
from calc_package.calculator import Calculator

calc = Calculator()

# add function. returns 2
calc.add(2)

# multiply function. returns 4
calc.multiply(2)

# subtract function. returns 2
calc.subtract(2)

# divide function. returns 1.0
calc.divide(2)

# reset function. returns 0
calc.reset()

# root function. returns 5, the squareroot of 25
calc.root(25,2)

```


## Functions
List the ready functions here:
- Add/Subtract function
- Multiply/Divide function
- Take nth root function
- Reset memory function



## Acknowledgements
Give credit here.
- This project was inspired by Turing College

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Project Status
Project is: _in progress_ 


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->

