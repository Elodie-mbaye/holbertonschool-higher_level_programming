class BaseGeometry:
    """BaseGeometry class with integer validation."""
    def integer_validator(self, name, value):
        """Validates that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initializes width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
