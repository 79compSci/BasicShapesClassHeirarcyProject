"""Demonstrate inheritance and runtime polymorphism with geometric shapes."""

from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    """Create shapes and demonstrate polymorphic processing."""
    circle1 = Circle(0, 0, 4)
    circle2 = Circle(5, 3, 2)
    rectangle1 = Rectangle(10, 5)
    rectangle2 = Rectangle(7, 3)
    square = Square(6)

    shapes = [circle1, circle2, rectangle1, rectangle2, square]

    print("SHAPE COLLECTION")
    print("----------------")
    for shape in shapes:
        print(f"{shape.name}: area = {shape.area:.2f}")

    print("\nCIRCLE CHANGE")
    print(f"Before: radius = {circle1.radius}, area = {circle1.area:.2f}")
    circle1.radius = 8
    print(f"After:  radius = {circle1.radius}, area = {circle1.area:.2f}")

    print("\nRECTANGLE CHANGE")
    print(f"Before: length = {rectangle1.length}, width = {rectangle1.width}, area = {rectangle1.area:.2f}")
    rectangle1.length = 12
    rectangle1.width = 8
    print(f"After:  length = {rectangle1.length}, width = {rectangle1.width}, area = {rectangle1.area:.2f}")

    print("\nSQUARE CHANGE")
    print(f"Before: side = {square.side}, length = {square.length}, width = {square.width}, area = {square.area:.2f}")
    square.side = 10
    print(f"After:  side = {square.side}, length = {square.length}, width = {square.width}, area = {square.area:.2f}")


if __name__ == "__main__":
    main()
