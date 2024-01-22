"""module Class Square"""
from src.rectangle import Figure


class Square(Figure):
    """Class Square"""

    def __init__(self, side_a):
        super().__init__(name="Square")
        if side_a <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.__side_a = side_a

    @property
    def side_a(self):
        """Getter for attribute __side_a"""
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        """Setter for attribute __side_a"""
        self.__side_a = value

    def get_area(self):
        """method get_area"""
        return self.__side_a * self.__side_a

    def get_perimeter(self):
        """method get_perimeter"""
        return 4 * self.__side_a

    def __str__(self):
        """Метод описания (description)"""
        return f"Square with side: {self.side_a}"
