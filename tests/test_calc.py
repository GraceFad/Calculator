from src.calc_package.calculator import Calculator
calculator = Calculator()

def test_can_add_number():
    # CHECK IF CALCULATOR CAN ADD NUMBER TO MEMORY VALUE 
    assert calculator.add(2) == 2.0

def test_can_subtract_number():
    # CHECK IF CALCULATOR CAN SUBTRACT NUMBER TO MEMORY VALUE 
    assert calculator.subtract(1) == 1

def test_can_divide_number():
    # CHECK IF CALCULATOR CAN DIVIDE MEMORY VALUE BY THE NUMBER
    assert calculator.divide(2) == 0.5

def test_can_multiply_number():
    # CHECK IF CALCULATOR CAN MULTIPLY MEMORY VALUE BY THE NUMBER
    assert calculator.multiply(2) == 1

def test_can_take_the_nth_root_of_number():
    # CHECK IF CALCULATOR CAN TAKE THE NUMBER ROOT OF THE MEMORY VALUE 
    assert calculator.root(1, 2) == 1

def test_can_reset_memory_to_default():
    # CHECK IF CALCULATOR CAN RESET MEMORY VALUE TO 0
    assert calculator.reset() == 0

def test_can_raise_exception_error():
    # CHECK IF CALCULATOR CAN RAISE INSTANCE ERROR FOR WRONG NUMBER INPUT
    assert calculator.add('aa') == 'This is a wrong input. Input a float or integer'
