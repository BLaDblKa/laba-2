import math

class GeometricFigure:
    def area(self):
        pass

    def perimeter(self):
        pass

class Ellipse(GeometricFigure):
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        return math.pi * self.major_axis * self.minor_axis

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.major_axis ** 2 + self.minor_axis ** 2) / 2)

class Square(GeometricFigure):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Trapezoid(GeometricFigure):
    def __init__(self, base1, base2, height, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

# Демонстрация работы
choice = input("Выберите тип фигуры (1 - эллипс, 2 - квадрат, 3 - трапеция): ")

if choice == '1':
    major_axis = float(input("Введите большую полуось эллипса: "))
    minor_axis = float(input("Введите малую полуось эллипса: "))
    ellipse = Ellipse(major_axis, minor_axis)
    print("Площадь эллипса:", ellipse.area())
    print("Периметр эллипса:", ellipse.perimeter())
elif choice == '2':
    side_length = float(input("Введите длину стороны квадрата: "))
    square = Square(side_length)
    print("Площадь квадрата:", square.area())
    print("Периметр квадрата:", square.perimeter())
elif choice == '3':
    base1 = float(input("Введите длину первого основания трапеции: "))
    base2 = float(input("Введите длину второго основания трапеции: "))
    height = float(input("Введите высоту трапеции: "))
    side1 = float(input("Введите первое боковое ребро трапеции: "))
    side2 = float(input("Введите второе боковое ребро трапеции: "))
    trapezoid = Trapezoid(base1, base2, height, side1, side2)
    print("Площадь трапеции:", trapezoid.area())
    print("Периметр трапеции:", trapezoid.perimeter())
else:
    print("Неверный выбор")