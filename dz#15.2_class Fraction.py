class Fraction:
    """Fraction class"""

    def __init__(self, a:int, b:int):
        if b == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        if b < 0:
            a, b = -a, -b
        self.a = a
        self.b = b
    #     self.simplify() #auto simplify a fraction
    #
    # def simplify(self):
    #     """Simplify a fraction"""
    #     gcd = self.greatest_common_divisor(self.a, self.b)
    #     self.a //= gcd
    #     self.b //= gcd
    #
    # @staticmethod
    # def greatest_common_divisor(a, b):
    #     while b:
    #         a, b = b, a % b  #Euclidean algorithm for finding the greatest common divisor (GCD)
    #     return abs(a)

    def __mul__(self, other):
        """Multiplication of two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        """Division of two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.a * other.b, self.b * other.a)

    def __add__(self, other):
        """Addition of two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = self.a * other.b + self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Subtraction of two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = self.a * other.b - self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Comparison of two fractions"""
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented

    def __gt__(self, other):
        """Comparison of two fractions"""
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented

    def __lt__(self, other):
        """Comparison of two fractions"""
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return NotImplemented

    def __str__(self):
        if self.a == 0:
            return "Fraction: 0"
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

f_a = Fraction(4, -9)
f_b = Fraction(3, 7)
f_l = f_b + f_a
print(f_l)
f_r = f_b/f_a
print(f_r)
f_p = f_b - f_a
print(f_p)