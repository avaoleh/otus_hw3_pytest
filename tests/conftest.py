import pytest

data_int_rectangle = (3, 5, 15, 16)
data_float_rectangle = (3.5, 5.5, 19.25, 18.0)

data_int_square = (5, 25, 20)
data_float_square = (5.0, 25.0, 20.0)

data_int_circle = (7, 153.94, 43.98)
data_float_circle = (7.0, 153.94, 43.98)

data_int_triangle = (3, 4, 5, 6, 12)
data_float_triangle = (3.0, 4.0, 5.0, 6.0, 12.0)


@pytest.fixture(scope="function")
def start_db():
    print("\n Start DB")
    yield
    print("\n Stop DB")


@pytest.fixture(scope="function")
def get_rectangle(start_db):
    print("\n Start Calc Rectangle")

    def _wrapper(value: str):
        if value == "int":
            return data_int_rectangle
        elif value == "float":
            return data_float_rectangle
        else:
            raise AssertionError("Only int or float valid data")

    yield _wrapper

    print("\n Stop Calc Rectangle")


@pytest.fixture(scope="function")
def get_square(start_db):
    print("\n Start Calc Square")

    def _wrapper(value: str):
        if value == "int":
            return data_int_square
        elif value == "float":
            return data_float_square
        else:
            raise AssertionError("Only int or float valid data")

    yield _wrapper

    print("\n Stop Calc Square")


@pytest.fixture(scope="function")
def get_circle(start_db):
    print("\n Start Calc Circle")

    def _wrapper(value: str):
        if value == "int":
            return data_int_circle
        elif value == "float":
            return data_float_circle
        else:
            raise AssertionError("Only int or float valid data")

    yield _wrapper

    print("\n Stop Calc Circle")


@pytest.fixture(scope="function")
def get_triangle(start_db):
    print("\n Start Calc Triangle")

    def _wrapper(value: str):
        if value == "int":
            return data_int_triangle
        elif value == "float":
            return data_float_triangle
        else:
            raise AssertionError("Only int or float valid data")

    yield _wrapper

    print("\n Stop Calc Triangle")
