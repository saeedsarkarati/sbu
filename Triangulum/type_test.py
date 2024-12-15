from enum import Enum
# ~ from typing import Union

class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2

class Size(Enum):
    SMALL = 1
    MEDIUM = 2



# Example usage
selected_shape: Shape = Shape.CIRCLE
print(selected_shape)

selected_size: Size = Size.MEDIUM
print(selected_size)
