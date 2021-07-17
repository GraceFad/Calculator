from src.calc_package.calculator import Calculator

def test_can_add_number():
    calculator = Calculator()
    assert calculator.add(2) == 2.0

def test_can_subtract_number():
    calculator = Calculator()
    assert calculator.subtract(1) == -1

def test_can_divide_number():
    calculator = Calculator()
    assert calculator.divide(2) == 0

def test_can_multiply_number():
    calculator = Calculator()
    assert calculator.multiply(2) == 0

def test_can_take_the_nth_root_of_number():
    calculator = Calculator()
    assert calculator.root(1, 2) == 1

def test_can_reset_memory_to_default():
    calculator = Calculator()
    assert calculator.reset() == 0

def test_can_raise_exception_error():
    # CHECK IF CALCULATOR CAN RAISE INSTANCE ERROR FOR DIFFERENT WRONG NUMBER INSTANCES
    calculator = Calculator()
    assert calculator.add('aa') == 'This is a wrong input. Input a float or integer'
    assert calculator.divide(0) == "Input a number greater than 0 "
    assert calculator.root(0,5) == "Input a value greater than 0 "
    assert calculator.root(0,'aa') == "Input a value greater than 0 "
    

