"""Define the Rectangle class for the basic-shapes hierarchy."""

from basic_shape import BasicShape


class Rectangle(BasicShape):
    """Represent a rectangle that inherits from BasicShape."""

    def __init__(self, length, width, name="Rectangle"):
        """Initialize a rectangle with positive length and width."""
        super().__init__(name)
        self._length = None
        self._width = None
        self.length = length
        self.width = width

    @property
    def length(self):
        """Return the rectangle's length."""
        return self._length

    @length.setter
    def length(self, value):
        """Set a positive numeric length and recalculate area when possible."""
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be numeric.")
        if value <= 0:
            raise ValueError("Length must be greater than zero.")
        self._length = value
        if self._width is not None:
            self.calc_area()

    @property
    def width(self):
        """Return the rectangle's width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set a positive numeric width and recalculate area when possible."""
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be numeric.")
        if value <= 0:
            raise ValueError("Width must be greater than zero.")
        self._width = value
        if self._length is not None:
            self.calc_area()

    def calc_area(self):
        """Calculate and store the rectangle's area."""
        self._area = self._length * self._width
        return self._area
