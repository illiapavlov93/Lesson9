import math


class Figure(object):

    def __init__(self, sides):
        self.sides = sides

    def perimeter(self, sides):
        raise NotImplementedError('perimeter not implemented in Figure')

    def area(self, sides):
        raise NotImplementedError('area not implemented in Figure')


class Triangle(Figure):
    def __init__(self, sides):
        if len(sides) != 3:
            raise Exception('Triangle takes exactly 3 sides')
        super(Triangle, self).__init__(sides)

    def perimeter(self):
        p = sum(self.sides)
        return p

    def area(self):
        half_p = self.perimeter() * 0.5
        ar = half_p
        for side in self.sides:
            ar *= half_p - side
        ar = ar ** 0.5
        return ar


t = Triangle([3, 4, 5])
print(t.perimeter())
print(t.area())


class Rectangle(Figure):
    def __init__(self, sides):
        if len(sides) != 2:
            raise Exception('Rectangle takes exactly 2 sides')
        super().__init__(sides)

    def perimeter(self):
        p = sum(self.sides) * 2
        return p

    def area(self):
        ar = self.sides[0] * self.sides[1]
        return ar


r = Rectangle([4, 7])
print(r.perimeter())
print(r.area())


class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            print('Circle: radius must be numeric')
            raise Exception()
        self.r = radius

    def perimeter(self):
        p = 2 * self.r * math.pi
        return p

    def area(self):
        ar = math.pi * self.r ** 2
        return ar


c = Circle(100)
print(c.perimeter())
print(c.area())
