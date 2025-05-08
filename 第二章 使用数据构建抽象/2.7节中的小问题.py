# class Number:
#     # 这里以双下划线命名的方法被称为“魔法方法”或“双下方法”，主要用于实现类的特殊行为（如运算符重载、对象构造、上下文管理等）
#     def __add__(self,other): # 双下划线命名是Python的保留机制，确保这个方法不会被普通方法名意外覆盖
#         return self.add(other) # 实际的加法逻辑委托给子类实现
#     def __mul__(self,other):
#         return self.mul(other) # 实际的乘法逻辑委托给子类实现





def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)
def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


class Number:
    def __add__(self, other):
        if hasattr(self, 'type_tag') and hasattr(other, 'type_tag'):
            if self.type_tag == other.type_tag:
                return self.add(other)
            elif (self.type_tag, other.type_tag) in self.adders:
                return self.cross_apply(other, self.adders)
        raise TypeError("Unsupported operand types for +")
    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)
    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)
    adders = {("com", "rat"): add_complex_and_rational,
        ("rat", "com"): add_rational_and_complex
    }
    multipliers = {("com", "rat"): mul_complex_and_rational,
                   ("rat", "com"): mul_rational_and_complex}

class Complex(Number):
    type_tag = "com"
    def add(self,other):
        return ComplexRI(self.real+other.real,self.imag+other.imag)
    def mul(self,other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude,self.angle+other.angle)

from math import atan2
class ComplexRI(Complex):
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real**2 + self.imag**2) **0.5
    @property
    def angle(self):
        return atan2(self.imag,self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real,self.imag)

from math import sin,cos,pi
class ComplexMA(Complex):
    def __init__(self,magnitude,angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude*cos(self.angle)
    @property
    def imag(self):
        return self.magnitude*sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g}*pi)'.format(self.magnitude,self.angle/pi)

from math import gcd
class Rational(Number):
    type_tag = "rat"
    def __init__(self, numer, denom):
        g = gcd(numer, denom) # 计算最大公约数
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)
    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

print(ComplexRI(1.5, 0) + Rational(3, 2))