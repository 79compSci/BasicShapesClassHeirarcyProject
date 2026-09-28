"""Define the abstract BasicShape class for the shape hierarchy."""

from abc import ABC, abstractmethod


class BasicShape(ABC):
    """Represent the common interface shared by all geometric shapes."""

    def __init__(self, name):
        """Initialize a shape with a validated name and initial area."""
        self._area = 0.0
        self.name = name

    @property
    def name(self):
        """Return the name of the shape."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the shape name to a nonempty string."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def area(self):
        """Return the current calculated area."""
        return self._area

    @abstractmethod
    def calc_area(self):
        """Calculate and store the area of the shape."""
        pass
