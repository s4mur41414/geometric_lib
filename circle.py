import math


def area(r):
    '''
    Calculates the area of a circle.
    
        Parameters:
            r (int/float): radius of the circle

        Returns: 
            area (int/float): the area of the circle with radius r

        Example:
            'area(5)' returns  78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the perimeter of a circle.

        Parameters:
            r (int/float): radius of the circle

        Returns:
            perimeter (int/float): the perimeter of the circle with radius r

        Example:
            'perimeter(5)' returns 31.41592653589793
    '''
    return 2 * math.pi * r