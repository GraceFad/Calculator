class Calculator:
    """
    A class to perform simple add/subtract, divide/mulitply functions, take the nth root of a number and reset memory value.

    ...

    Attributes
    ----------
    value : 0
        memory value of the calculator

    Methods
    -------
    add(self, num: int or float) -> int or float:
        Adds the value inputted to the memory value.
    subtract(self, num: int or float) -> int or float:
        Subtracts the value inputted from the memory value.
    divide(self, num: int or float) -> int or float:
        Divides the memory value by the value inputted.
    multiply(self, num: int or float) -> int or float:
        Muliplies the value inputted by the memory value.
    root(self, num: int or float, rootnum: int or float) -> int or float:
        Returns the number inputted to the root of the inversed rootnum.
    reset(self):
        Resets the memory value to 0.

    """

    def __init__(self):
        self._value = 0
    
    @property
    def value(self):
        """int: Returns the memory value at a particular time"""
        return self._value

    def add(self, num: int or float) -> int or float:
        """
        A function to add a number to the memory.  

            Args:
                num: The parameter to be added to current memory value.
            Returns:
                The return value. Sum of number inputted and memory value.
        """
        if isinstance (num, (int, float)):
            self._value += num
            return self._value
        else:
            return ('This is a wrong input. Input a float or integer')

    def subtract(self, num: int or float) -> int or float:
        """
        A function to subtract a number from the memory.  

        Args:
            num: The parameter to be subtracted from the current memory value.

        Returns:
            The return value gotten from the subtraction of inputted number and the menory value.
        """
        if isinstance (num, (int, float)):
            self._value -= num
            return self._value
        else:
            return ('This is a wrong input. Input a float or integer')

    def multiply(self, num: int or float) -> int or float:
        """
        A function to multiply memory value and number inputted .  

            Parameters:
                num: The parameter to be multiplied by the current memory value.

            Returns:
                The return value. Product of number inputted and memory value.
        """
        if isinstance (num, (int, float)):
            self._value *= num
            return self._value
        else:
            return ('This is a wrong input. Input a float or integer')

    def divide(self, num: int or float)-> int or float:
        """
        A function to divide the memory by a number.  

            Args:
                num: The parameter to divide the current memory value.

            Returns:
                The return value. Division of memory value by number inputted.
        """
        if num == 0:
            return ("Input a number greater than 0 ")
        else: 
            if isinstance (num, (int, float)):
                self._value /= num
                return self._value
            else:
                return ('This is a wrong input. Input a float or integer')
 
    def root(self, num: int or float, rootnum: int or float) -> int or float :
        """
        Returns the number inputted to the root of the inversed rootnum.

            Parameters:
                    num (int or float): An integer ot float
                    rootnum (int or float): Another integer or float to serve as the root number.

            Returns:
                    The root of the num.
        """
        import math 
        if num == 0 or rootnum == 0:
            return ("Input a value greater than 0 ")
        else:
            return num ** (1/rootnum)

    def reset(self):
        """
        Resets the memory value to 0.

            Parameters:
                    num (int or float): An integer ot float
                    rootnum (int or float): Another integer or float to serve as the root number.

            Returns:
                    The root of the num.
        """
        self._value = 0
        return self.value 
        