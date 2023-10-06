import math


def area(r):
    '''
    Calculates the area of a circle.
    
        Parameters:
            r (int/float): radius of the circle

        Returns: 
            area (int/float): the area of the circle with radius r
        '''
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the perimeter of a circle.

            Parameters:
                r (int/float): radius of the circle

            Returns:
                perimeter (int/float): the perimeter of the circle with radius r
            '''
    return 2 * math.pi * r

