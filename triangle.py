def area(a, h):
    '''
    Calculates the area of a triangle.

       Parameters:
           a (int/float): side of the triangle
           h (int/float): height drawn to the side a in triangle

       Returns:
           area (int/float): the area of the triangle with side a and height h

        Example:
            'area(2, 3)' returns 3
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
   Calculates the perimeter of a triangle.

       Parameters:
           a (int/float): first side of the triangle
           b (int/float): second side of the triangle
           c (int/float): third side of the triangle

       Returns:
           perimeter (int/float): the perimeter of the triangle with sides a, b and c

        Example:
            'perimeter(2, 3, 4)' returns 9
    '''
    return a + b + c
