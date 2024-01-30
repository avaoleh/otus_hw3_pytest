"""module Class Circle"""
import math
from src.figure import Figure


class Circle(Figure):
    """Class Circle"""

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("нельзя создать круг")
        super().__init__(name="Rectangle")
        self.__radius = radius

    @property
    def radius(self):
        """Getter for attribute radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Setter for attribute radius"""
        self.__radius = value

    def get_area(self):
        """method get_area"""
        return round(math.pi * (self.__radius**2), 2)

    def get_perimeter(self):
        """method get_perimeter"""
        return round(2 * math.pi * self.__radius, 2)

    def __str__(self):
        """Метод описания (description)"""
        return f"Circle with radius: {self.__radius} "
