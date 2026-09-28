"""Define the Circle class for the basic-shapes hierarchy."""

import math
from basic_shape import BasicShape


class Circle(BasicShape):
    """Represent a circle that inherits from BasicShape."""

    def __init__(self, x_center, y_center, radius, name="Circle"):
        """Initialize a circle with a center point and positive radius."""
        super().__init__(name)
        self._radius = None
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    @property
    def x_center(self):
        """Return the x-coordinate of the circle's center."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        """Set the x-coordinate to a numeric value."""
        if not isinstance(value, (int, float)):
            raise TypeError("x_center must be numeric.")
        self._x_center = value

    @property
    def y_center(self):
        """Return the y-coordinate of the circle's center."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        """Set the y-coordinate to a numeric value."""
        if not isinstance(value, (int, float)):
            raise TypeError("y_center must be numeric.")
        self._y_center = value

    @property
    def radius(self):
        """Return the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set a positive numeric radius and automatically recalculate area."""
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be numeric.")
        if value <= 0:
            raise ValueError("Radius must be greater than zero.")
        self._radius = value
        self.calc_area()

    def calc_area(self):
        """Calculate and store the circle's area."""
        self._area = math.pi * self._radius ** 2
        return self._area
