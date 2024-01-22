"""module Class Triangle"""
import math
from src.figure import Figure


class Triangle(Figure):
    """Class Triangle"""

    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("нельзя создать треугольник")
        if not (
            side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a
        ):
            raise ValueError("нельзя создать треугольник")
        super().__init__(name="Triangle")
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    @property
    def side_a(self):
        """Getter for attribute __side_a"""
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        """Setter for attribute __side_a"""
        self.__side_a = value

    @property
    def side_b(self):
        """Getter for attribute side_b"""
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        """Setter for attribute side_b"""
        self.__side_b = value

    @property
    def side_c(self):
        """Getter for attribute side_c"""
        return self.__side_c

    @side_c.setter
    def side_c(self, value):
        """Setter for attribute side_c"""
        self.__side_c = value

    def get_perimeter(self):
        """method get_perimeter"""
        return self.__side_a + self.__side_b + self.__side_c

    def get_area(self):
        """method get_area"""
        phalf = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(
            phalf
            * (phalf - self.__side_a)
            * (phalf - self.__side_b)
            * (phalf - self.__side_c)
        )

    def __str__(self):
        """Метод описания (description)"""
        return f"Triangle with sides: {self.__side_a}, {self.__side_b}, {self.__side_c}"
