import math
import sys
# OPERATOR OVERLOADING
class Fraction:
    
    def __init__(self, num, den = 1):
        if den == 0:
            raise ValueError("Denominator can't be 0")
            sys.exit()
        elif den < 0:
            # don't allow for negative denominators
            den *= -1
            num *= -1
        self.num = num
        self.den = den
        self.reduceFrac()
    
    def gcd(self, m, n):
        # euclids method for finding gcd of M and N
        r = m % n
        while r != 0:
            m = n
            n = r
            r = m % n
        return n
    
    def reduceFrac(self):
        gcd = self.gcd(self.num, self.den)
        self.num /= gcd
        self.den /= gcd
        if self.den < 0:
            self.den *= -1
            self.num *= -1
        self.num = int(self.num)
        self.den = int(self.den)

    def castFrac(self, other):
        if not isinstance(other, Fraction):
            try:
                other = Fraction(int(other))
            except Exception as e:
                print(e)
                sys.exit()
        return other
    
    # Overload <
    def __lt__(self, other):
        other = self.castFrac(other)
        self.reduceFrac()
        other.reduceFrac()
        return (self.num * other.den) < (other.num * self.den)

    # Overload >
    def __gt__(self, other):
        other = self.castFrac(other)
        self.reduceFrac()
        other.reduceFrac()
        return (self.num * other.den) > (other.num * self.den)

    # Overload ==
    def __eq__(self, other):
        other = self.castFrac(other)
        self.reduceFrac()
        other.reduceFrac()
        return (self.num * other.den) == (other.num * self.den)

    # Overload +
    def __add__(self, other):
        other = self.castFrac(other)
        den = self.den * other.den
        num = (self.num * other.den) + (self.den * other.num)
        return Fraction(num, den)

    # Overload -
    def __sub__(self, other):
        other = self.castFrac(other)
        den = self.den * other.den
        num = (self.num * other.den) - (self.den * other.num)
        return Fraction(num, den)

    # Overload *
    def __mul__(self, other):
        other = self.castFrac(other)
        den = self.den * other.den
        num = self.num * other.num
        return Fraction(num, den)
    
    # Overload /
    def __truediv__(self, other):
        other = self.castFrac(other)
        otherInv = Fraction(other.den, other.num)
        return self * otherInv

    # Overload **
    def __pow__(self, exp):
        return Fraction(self.num**exp, self.den**exp)
    
    # Overload str()
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    # Overload -Fraction
    def __neg__(self):
        return Fraction(-1 * self.num, self.den)
    
    # Overload abs(Fraction)
    def __abs__(self):
        return Fraction(abs(self.num), self.den)

    # Overload math.floor(Fraction)
    def __floor__(self):
        return self.num//self.den
    
    # Overload math.ceil(Fraction)
    def __ceil__(self):
        return math.ceil(self.num/self.den)

    # Overload int(Fraction)
    def __int__(self):
        return int(float(self))

    # Overload float(Fraction)
    def __float__(self):
        return self.num/self.den


if __name__ == "__main__":
    a = Fraction(2, 4)
    b = Fraction(1, 3)
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)
    print(a, "<", b, "=", a<b)
    print(a, ">", b, "=", a>b)
    print(a, "=", b, "=", a==b)
    a+=b
    print(a)
    print(a, "^ 2 =", a**2)
    print("negative",a, "=", -a)
    print("int(",a*3, ") =", int(a*3))
    print("float(",a, ") =", float(a))
    print("Floor:",math.ceil(a), "Ceil:",math.floor(a))
    print("|",a, "* -11 | =", abs(a*-11))
    print(math.floor(a*"asd"))