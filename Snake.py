# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program to store x and y parameter variables for "S" i.e. snake symbol.

from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")
