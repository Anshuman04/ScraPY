# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, {self.name}!")

#     def age_after_5_years(self):
#         return self.age + 5
    
#     def print_age_after_5_years(self):
#         future_age = self.age_after_5_years()
#         print(f"After 5 years, {self.name} will be {future_age} years old.")


# person1 = Person("Anshu", 30)
# person2 = Person("Nix", 26)

# person1.greet()
# person2.greet()

# person1.print_age_after_5_years()
# person2.print_age_after_5_years()

"""
object -> int
object -> str
object -> Person
object -> Geometry
object -> Geometry -> Square
object -> Geometry -> Rectangle
"""

class Geometry:
    def __init__(self):
        self.all_sides = []
    
    def perimeter(self):
        result = 0
        for item in self.all_sides:
            result = result + item
        return result

    def new_func(self):
        pass

class Square(Geometry):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.setup_square()
    
    def setup_square(self):
        self.all_sides.append(self.side)
        self.all_sides.append(self.side)
        self.all_sides.append(self.side)
        self.all_sides.append(self.side)
    
    def area(self):
        return self.side * self.side

class Rectangle(Geometry):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.setup_rectangle()
    
    def setup_rectangle(self):
        self.all_sides.append(self.length)
        self.all_sides.append(self.width)
        self.all_sides.append(self.length)
        self.all_sides.append(self.width)
    
    def area(self):
        return self.length * self.width

class Circle(Geometry):
    def __init__(self, radius):
        import pdb; pdb.set_trace()
        super().__init__()
        self.radius = radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class SemiCircle(Circle):
    def __init__(self, radius):
        super().__init__(radius)
    
    def area(self):
        return super().area() / 2

square = Square(10)
rectangle = Rectangle(10, 20)
circle = Circle(10)

print(square.perimeter())
print(rectangle.perimeter())
print(circle.perimeter())