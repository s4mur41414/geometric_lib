def area(a, b):
    '''
    Calculates the area of a rectangle.
            
        Parameters:
            a (int/float): first side of the rectangle
            b (int/float): second side of the rectangle

        Returns:
            area (int/float): the area of the rectangle with sides a and b

        Example:
            'area(2, 3)' returns 6
    '''
    return a * b


def perimeter(a, b):
    '''
    Calculates the perimeter of a rectangle.

        Parameters:
            a (int/float): first side of the rectangle
            b (int/float): second side of the rectangle

        Returns:
            perimeter (int/float): the perimeter of the rectangle with sides a and b

        Example:
            'perimeter(2, 3)' returns 10
    '''
    return 2 * (a + b)