from modules.calculator import Calculator
calculator = Calculator()

def test_can_add_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.add(2) == 2.0

def test_can_subtract_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.subtract(1) == 1

def test_can_divide_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.divide(2) == 0.5

def test_can_multiply_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.multiply(2) == 1

def test_can_take_the_nth_root_of_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.root(1, 2) == 1