"""module Class abc Figure"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """Class abc Figure"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_area(self):
        """abs method get_area"""
        pass

    @abstractmethod
    def get_perimeter(self):
        """abs method get_perimeter"""
        pass

    def add_area(self, other_figure):
        """method add_area"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
