"""module Class Rectangle"""
from src.figure import Figure


class Rectangle(Figure):
    """Class Rectangle"""

    def __init__(self, side_a: int, side_b: int):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.__side_a = side_a
        self.__side_b = side_b

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

    def get_area(self):
        """method get_area"""
        area = self.__side_a * self.__side_b
        return area

    def get_perimeter(self):
        """method get_perimeter"""
        return 2 * (self.__side_a + self.__side_b)

    def __str__(self):
        """Метод описания (description)"""
        return f"Rectangle with sides: {self.__side_a} , {self.__side_b}"
