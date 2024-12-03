#include <iostream>
#include <string>
#include <cmath>

// Abstract Base Class: BasicShape
class BasicShape {
private:
    double area;
    std::string name;

protected:
    // Setter for area (accessible by derived classes)
    void setArea(double a) { area = a; }

    // Setter for name (accessible by derived classes)
    void setName(const std::string& n) { name = n; }

public:
    // Getter for area
    double getArea() const { return area; }

    // Getter for name
    std::string getName() const { return name; }

    // Pure virtual function to calculate area
    virtual void calcArea() = 0;

    // Virtual destructor
    virtual ~BasicShape() {}
};

// Derived Class: Circle
class Circle : public BasicShape {
private:
    double xCenter;
    double yCenter;
    double radius;

public:
    // Constructor
    Circle(double x, double y, double r, const std::string& n = "Circle")
        : xCenter(x), yCenter(y), radius(r) {
        setName(n);
        calcArea();  // Calculate and set the area
    }

    // Implement calcArea
    void calcArea() override {
        double area = M_PI * radius * radius;
        setArea(area);  // Use the base class setter
    }

    // Getters
    double getXCenter() const { return xCenter; }
    double getYCenter() const { return yCenter; }
    double getRadius() const { return radius; }
};

// Derived Class: Rectangle
class Rectangle : public BasicShape {
private:
    double length;
    double width;

public:
    // Constructor
    Rectangle(double l, double w, const std::string& n = "Rectangle")
        : length(l), width(w) {
        setName(n);
        calcArea();  // Calculate and set the area
    }

    // Implement calcArea
    void calcArea() override {
        double area = length * width;
        setArea(area);  // Use the base class setter
    }

    // Getters
    double getLength() const { return length; }
    double getWidth() const { return width; }
};

// Derived Class: Square
class Square : public Rectangle {
private:
    double side;

public:
    // Constructor
    Square(double s, const std::string& n = "Square")
        : Rectangle(s, s, n), side(s) {
        setName(n);  // Set the name in the base class
    }

    // Getter for side
    double getSide() const { return side; }
};

int main() {
    // Test the Circle class
    Circle circle(5.0, 5.0, 10.0);
    std::cout << "Shape: " << circle.getName() << "\n"
              << "Center: (" << circle.getXCenter() << ", " << circle.getYCenter() << ")\n"
              << "Radius: " << circle.getRadius() << "\n"
              << "Area: " << circle.getArea() << "\n\n";

    // Test the Rectangle class
    Rectangle rectangle(10.0, 5.0);
    std::cout << "Shape: " << rectangle.getName() << "\n"
              << "Length: " << rectangle.getLength() << "\n"
              << "Width: " << rectangle.getWidth() << "\n"
              << "Area: " << rectangle.getArea() << "\n\n";

    // Test the Square class
    Square square(4.0);
    std::cout << "Shape: " << square.getName() << "\n"
              << "Side: " << square.getSide() << "\n"
              << "Area: " << square.getArea() << "\n";

    return 0;
}