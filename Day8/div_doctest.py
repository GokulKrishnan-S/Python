def floordiv(num1, num2):
    '''
    floor divison of numbers
    >>> print(floordiv(3, 3))
    1
    '''
    if num1 >= num2:
        return num1 // num2
    elif num1 < num2:
        return 0    


import doctest
doctest.testmod()
