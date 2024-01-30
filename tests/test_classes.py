import pytest

from src.circle import Circle
from src.triangle import Triangle
from src.square import Square
from src.rectangle import Rectangle


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_positive_rectangle(get_rectangle, value):
    a, b, area, perimeter = get_rectangle(value=value)
    r = Rectangle(a, b)
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_positive_square(get_square, value):
    a, area, perimeter = get_square(value=value)
    s = Square(a)
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_positive_circle(get_circle, value):
    a, area, perimeter = get_circle(value=value)
    c = Circle(a)
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_positive_triangle(get_triangle, value):
    a, b, c, area, perimeter = get_triangle(value=value)
    t = Triangle(a, b, c)
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [(-3, -5, 15), (-3.5, -5.5, 19.25)],
    ids=["int", "float"],
)
def test_negative_rectangle(side_a, side_b, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("side_a", [-5, -5.5], ids=["int", "float"])
def test_negative_square(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize("radius", [-5, -5.5], ids=["int", "float"])
def test_negative_circle(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(-3, -4, -5), (-3.5, -4.5, -5.5)],
    ids=["int", "float"],
)
def test_negative_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_calc_add_area():
    r = Rectangle(3, 5)
    c = Circle(5)
    s = Square(5)
    t = Triangle(3, 4, 5)

    assert r.add_area(c) == r.get_area() + c.get_area()
    assert c.add_area(t) == c.get_area() + t.get_area()
    assert t.add_area(s) == t.get_area() + s.get_area()
