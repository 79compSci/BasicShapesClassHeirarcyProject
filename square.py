"""Define the Square class for the basic-shapes hierarchy."""

from rectangle import Rectangle


class Square(Rectangle):
    """Represent a square while preserving equal side dimensions."""

    def __init__(self, side, name="Square"):
        """Initialize a square with one positive side value."""
        self._side = None
        super().__init__(side, side, name)
        self._side = side

    @property
    def side(self):
        """Return the square's side length."""
        return self._side

    @side.setter
    def side(self, value):
        """Set side, length, width, and area using one positive value."""
        self._validate_side(value)
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()

    @property
    def length(self):
        """Return the square's length."""
        return self._length

    @length.setter
    def length(self, value):
        """Set all square dimensions using the supplied length."""
        self._validate_side(value)
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()

    @property
    def width(self):
        """Return the square's width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set all square dimensions using the supplied width."""
        self._validate_side(value)
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()

    @staticmethod
    def _validate_side(value):
        """Validate that a square dimension is numeric and positive."""
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be numeric.")
        if value <= 0:
            raise ValueError("Side must be greater than zero.")
