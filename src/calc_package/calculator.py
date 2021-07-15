class Calculator:
    """
    """
    def __init__(self):
        self.__value = 0
    
    @property
    def value(self):
        """int: Returns the memory value at a particular time"""
        return self.__value

    def add(self, num: int or float) -> int or float:
        """
        A function to add a number to the memory.  
        Args:
            num: The parameter to be added to current memory value.
        Returns:
            The return value. Sum of number inputted and memory value.
        """
        if isinstance (num, (int, float)):
            self.__value += num
            return self.__value
        else:
            return ('This is a wrong input. Input a float or integer')
    
    def subtract(self, num: int or float) -> int or float:
        """
        A function to add a number to the memory.  
        Args:
            num: The parameter to be added to current memory value.
        Returns:
            The return value. Subtracted of number inputted and memory value.
        """

        self.__value = self.__value - num
        return self.__value

    def multiply(self, num: int or float) -> int or float:
        """
        A function to add a number to the memory.  
        Args:
            num: The parameter to be added to current memory value.
        Returns:
            The return value. Sum of number inputted and memory value.
        """

        self.__value = self.__value * num
        return self.__value

    def divide(self, num: int or float) -> int or float:
        self.__value = self.__value / num
        return self.__value

    def root(self, num: int or float, rootnum: int or float) -> int or float :
        import math 
        return num ** (1/rootnum)

    def reset(self):
        self.__value = 0
        return self.value 