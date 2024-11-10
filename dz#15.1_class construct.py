class Rectangle:
    """Class for rectangle"""

    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))): #Erorr Check
            raise ValueError("Just a numbers")
        if width <= 0 or height <= 0:                          #Erorr Check
            raise ValueError("Just a positive value")
        self.width = width
        self.height = height

    def get_square(self):
        """Get the area of the rectangle"""
        return self.width * self.height

    def __eq__(self, other):
        """Comparison of rectangle"""
        if not isinstance(other, Rectangle):   #Erorr Check
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """Adding two rectangles(combine their for Total Area)"""
        if not isinstance(other, Rectangle):    #Erorr Check
            return NotImplemented
        combined_area = self.get_square() + other.get_square()
        ratio = (self.width / self.height + other.width / other.height) / 2 #Calculates the average aspect ratio of two rectangles
        width = (combined_area * ratio) ** 0.5
        height = combined_area / width     #This ensures that the resulting area remains correct.
        return Rectangle(width, height)


    def __mul__(self, n):
        """Scale the area of the base Rectangle by n times"""
        if not isinstance(n, (int, float)):
            return NotImplemented                        #Erorr Check
        if n <= 0:
            raise ValueError("Must be a positive numeric value")
        scale_factor = n ** 0.5
        return Rectangle(self.width * scale_factor, self.height * scale_factor)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print('Ok!')


